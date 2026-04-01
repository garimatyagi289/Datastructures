# class Node:
#     def __init__(self, data=None, next=None):
#         self.data= data
#         self.next=None
# class ssl:
#     def __init__(self, head=None):
#         self.head =head

#     def insert_at_begining(self, data):
#         new_node=Node(data, self.head)
#         self.head=new_node

#     def insert_at_end(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head= new_node
#             return
#         last= self.head
#         while last.next:

#             last=last.next
#         last.next=new_node 

#     def display(self):
#         tem = self.head
#         while tem:
#             print(tem.data, end="")    
#             tem= tem.next 
#         print("none")    
# l1 = ssl()
# l1.insert_at_begining(10)
# l1.insert_at_end(20)
# l1.display()



# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev


# class DLL:
#     def __init__(self, head=None):
#         self.head = head

#     def insert_at_begining(self, data):
#         new_node = Node(data, self.head)
#         if self.head is not None:
#             self.head.prev = new_node
#         self.head = new_node

#     def insert_at_end(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
#         new_node.prev = last

#     def display(self):
#         tem = self.head
#         while tem:
#             print(tem.data, end=" <-> ")
#             tem = tem.next
#         print("None")

#     def insert_at_position(self, data, position):
#         new_node = Node(data)
#         if position == 0:
#             self.insert_at_begining(data)
#             return
#         tem = self.head
#         for _ in range(position - 1):
#             if tem is None:
#                 raise IndexError("Position out of bounds")
#             tem = tem.next
#         if tem is None:
#             raise IndexError("Position out of bounds")
#         new_node.next = tem.next
#         new_node.prev = tem
#         if tem.next is not None:
#             tem.next.prev = new_node
#         tem.next = new_node
# l1 = DLL()
# l1.insert_at_begining(10)
# l1.insert_at_end(20)
# l1.insert_at_position(15, 1)
# l1.display()

# class stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,data):    
#         self.stack.append(data)
#     def pop(self):
#         if len(stack)==0:
#             print("underflow")
#         else:
#             self.stack.pop()
#     def peek(self):
#         if len(self.stack) == 0:
#             print("underflow")

#     def empty(self):
#         if len(self.stack) == 0:
#             print("stack is empty")

#     def size(self):
#         print(len(self.stack))

#     def display(self):
#         while self.empty() == False:
#             print(self.peek())
#             self.pop()

# s = stack()
# s.pop()
# s.empty()
# s.push(12)
# s.push(121) 
# s.display(
    
# )                                       
    

# class Node:
#     def __init__(self, mydata):
#         self.data = mydata
#         self.address = None


# class LinkedList:
#     def __init__(self):
#         self.head = None


#     # Insert at First Position
#     def insertAtFirst(self, myData):
#         newNode = Node(myData)
#         newNode.address = self.head
#         self.head = newNode


#     # Insert at Last Position
#     def insertAtLast(self, myData):
#         newNode = Node(myData)

#         if self.head == None:
#             self.head = newNode
#             return

#         currentNode = self.head

#         while currentNode.address != None:
#             currentNode = currentNode.address

#         currentNode.address = newNode


#     # Insert at Position
#     def insertAtPosition(self, position, myData):

#         if position == 1:
#             self.insertAtFirst(myData)
#             return

#         newNode = Node(myData)
#         currentNode = self.head

#         for i in range(position - 2):
#             currentNode = currentNode.address

#         newNode.address = currentNode.address
#         currentNode.address = newNode


#     def deleteAtFirst(self):
#         if self.head != None:
#             self.head = self.head.address



# class Stack:

#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if len(self.stack) == 0:
#             print("Stack Underflow")
#         else:
#             return self.stack.pop()

#     def peek(self):
#         if len(self.stack) == 0:
#             print("Stack Underflow")
#         else:
#             return self.stack[-1]

#     def empty(self):
#         return len(self.stack) == 0

#     def size(self):
#         return len(self.stack)

#     def display(self):
#         if len(self.stack) == 0:
#             print("Stack is empty")
#         else:
#             for i in reversed(self.stack):
#                 print(i)


# # Creating object
# s = Stack()

# s.push(1)
# s.push(2)
# s.push(3)

# print("Stack elements:")
# s.display()

# print("Top element:", s.peek())
# print("Size:", s.size())

# s.pop()
# print("After pop:")
# s.display()            

#search input position

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         l = 0
#         r = len(nums) - 1
#         while l<=r:
#             mid = (l+r)//2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 l = mid + 1
#             else:
#              r = mid - 1
#         return l            
        

# #binary search
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l= 0
#         r= len(nums) - 1
#         mid= 1+r//2
#         while l<=r:
#             mid = (l+r)//2
#             if nums[mid]== target:
#                 return mid
#             elif nums[mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return -1                 
            

#merging two sorted lists  

# def merge_sort(arr):
#     if len(arr) <=1:
#         return arr
    
#     mid = len(arr)//2

#     l=merge_sort(arr[:mid])
#     r=merge_sort(arr[mid:])

#     return merge(l,r)

# def merge(l,r):
#     result = []
#     i=j=0

#     while i<len(l) and j<len(r):
#         if l[i]<r[j]:
#             result.append(l[i])
#             i += 1
#         else:
#             result.append(r[j])
#             j += 1

#     result.extend(l[i:])
#     result.extend(r[j:])

#     return result       

#selection sort

arr= [1,-2, 3, 0, -4, 7, 6, 2, 9]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
selection_sort(arr)
print(arr) 


#insertion sort

