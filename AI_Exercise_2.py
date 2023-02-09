#!/usr/bin/env python
# coding: utf-8

# In[9]:


# shortest chain 
from collections import deque
import time

# to reach 'startword' from 'endword' using BFS
def bfs(startword,endword, D):
    if startword == endword:
        return 0
    # target is not in the dictionary
    if target not in D:
        return 0

    # To store the current chain length
    level, wordlen = 0, len(start)

    # Push the starting word into the queue
    Q = deque()
    Q.append(start)

    # While the queue is non-empty
    while (len(Q) > 0):
        level += 1

        # Current size of the queue
        sizeofQ = len(Q)

        for i in range(sizeofQ):

        # Remove the first word from the queue
            word = [j for j in Q.popleft()]

            # For every character of the word
            for position in range(wordlen):
                # Retain the original character
                # at the current position
                orig_char = word[position]

                # Replace the current character  lowercase alphabet
                for c in range(ord('a'), ord('z')+1):
                    word[position] = chr(c)

                    # If the new word is equal
                    # to the target word
                    if ("".join(word) == target):
                        return level
                        # Remove the word from the set
                    # if it is found in it
                    if ("".join(word) not in D):
                        continue
        
                    del D["".join(word)]

                    # And push the newly generated word
                    # which will be a part of the chain
                    Q.append("".join(word))

                # Restore the original character
                # at the current position
                word[position] = orig_char
            print(Q)
    return 0

# Driver code
if __name__ == '__main__':
    l1 = ["fool", "pool", "foil", "foul", "cool", "poll", "fail", "pole", "pall", "pope", "pale", "page", "sale", "sage", "pipe", "doll", "soil", "soul", "nail", "jail", "tail", "bail", "fall"] 
    wordList = {}
    for i in l1:
        wordList[i]=1
        
    start = "pole"
    target = "soul"
    start_t = time.time()
    print("Length of shortest chain using BFS: ",
    bfs(start, target, wordList))
    end_t = time.time()
    print("Time taken by BFS",end_t - start_t)


# In[10]:


from collections import *
import string
from typing import List
import time

# wordlist dictionary
wList = ["fool", "pool", "foil", "foul", "cool", "poll", "fail", "pole", "pall", "pope", "pale", "page", "sale", "sage", "pipe", "doll", "soil", "soul", "nail", "jail", "tail", "bail", "fall"]

#intial word
startword = "pole"

#end word
endWord = "soul"



class Solution:
    
  def findLadders(self, startword: str, endWord: str, wList: List[str]) -> List[List[str]]:
    
# to reach 'target' from 'start' using DFS
    def dfs(word: str, path: List[str]) -> None:
    
      if word == endWord:
        result.append(path)
        return
      if word not in dict:
        return

      for c in dict[word]:
        dfs(c, path + [c])

    result = []
    wList = set(wList)
    
# if endword not in list
    if endWord not in wList:
      return result

    set_n = set([startword])
    dict = defaultdict(list)
    isFound = False

    while set_n and not isFound:
      for word in set_n:
        wList.discard(word)
      tempSet = set()
      for parent in set_n:
        for i in range(len(parent)):
            
          # Replace the current character  lowercase alphabet  
          for j in string.ascii_lowercase:
            newWord = parent[:i] + j + parent[i + 1:]
            if newWord == endWord:
                
              # And push the newly generated word
              # which will be a part of the chain
              dict[parent].append(newWord)
              isFound = True
            elif newWord in wList and not isFound:
              tempSet.add(newWord)
              dict[parent].append(newWord)
      set_n = tempSet

    if isFound:
      dfs(startword, [startword])
      print(type(result))
      return result[-1], len(result[-1])

start_t = time.time()
dfs= Solution()
end_t = time.time()
print("Time taken by DFS",end_t - start_t)


dfs.findLadders(startword, endWord, wList)


# In[ ]:




