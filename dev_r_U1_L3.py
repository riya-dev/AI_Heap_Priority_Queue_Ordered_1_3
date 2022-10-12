# Name: Riya S. Dev
# Date: 10/4/2020

import random

class HeapPriorityQueue():
   
   def __init__(self):
      self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
      self.current = 1        # to make this object iterable

   def next(self):            # define what __next__ does
      if self.current >=len(self.queue):
         self.current = 1     # to restart iteration later
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self
      
   __next__ = next

   def isEmpty(self):
      return len(self.queue) == 1    # b/c index 0 is dummy

   def swap(self, a, b):
      self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

   # Add a value to the heap_pq
   def push(self, value):
      self.queue.append(value)
      # write more code here to keep the min-heap property
      self.heapUp(len(self.queue)-1)

   # helper method for push      
   def heapUp(self, k):
      while k > 1: # ALL GOOD
         parent = k // 2
         # print("parent", self.queue[parent], "k", self.queue[k])
         if (self.queue[parent] < self.queue[k]): # if current larger than parent, swap
            return
         self.swap(parent, k)
         k = parent
               
   # helper method for reheap and pop
   def heapDown(self, k, size):
      left, right = 2 * k, 2 * k + 1

      if left == size and self.queue[k] > self.queue[size]: # last case
         self.swap(k, size)
      
      elif right <= size:
         min = (left if self.queue[left] <= self.queue[right] else right)
   
         if self.queue[k] > self.queue[min]:
            self.swap(k, min)
            self.heapDown(min, size)
   
   # make the queue as a min-heap            
   def reheap(self):
      for x in range(len(self.queue)//2, 0, -1):
         self.heapDown(x, size)
   
   # remove the min value (root of the heap)
   # return the removed value            
   def pop(self):
      # Your code goes here
      self.swap(1, len(self.queue)-1)
      pop = self.queue.pop()
      self.heapDown(1, len(self.queue)-1)
      return pop
      
   # remove a value at the given index (assume index 0 is the root)
   # return the removed value   
   def remove(self, index):
      # Your code goes here
      self.swap(index + 1, len(self.queue)-1) #swap with last index, index + 1 because of dummy
      pop = self.queue.pop()
      self.heapDown(index + 1, len(self.queue)-1)
      return pop

# This method is for testing. Do not change it.
def isHeap(heap, k):
   left, right = 2*k, 2*k+1
   if left == len(heap): return True
   elif len(heap) == right and heap[k] > heap[left]: return False
   elif right < len(heap): 
      if (heap[k] > heap[left] or heap[k] > heap[right]): return False
      else: return isHeap(heap, left) and isHeap(heap, right)
   return True
    
# This method is for testing. Do not change it.
def main():
        
   pq = HeapPriorityQueue()    # create a HeapPriorityQueue object
   
   print ("Check if dummy 0 is still dummy:", pq.queue[0])
   
   # assign random integers into the pq
   for i in range(20):
      t = random.randint(10, 99)
      print (t, end=" ")
      pq.push(t)
   
   print ()
   
   # print the pq which is a min-heap
   for x in pq:
      print (x, end=" ")
   print()
   
   # remove test
   print ("Index 4 is removed:", pq.remove(4))
   
   # check if pq is a min-heap
   for x in pq:
      print (x, end=" ")
   print("\nIs a min-heap?", isHeap(pq.queue, 1))
   
   temp = []
   while not pq.isEmpty():
      temp.append(pq.pop())
      print (temp[-1], end=" ")
   
   print ("\nIn ascending order?", temp == sorted(temp))

if __name__ == '__main__':
   main()