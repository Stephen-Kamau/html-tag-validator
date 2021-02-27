import re
import datetime


class Node:
    """
    Initialize a node with only next and value
    """
    def __init__(self, value):
      self.value = value
      self.next = None

class Stack:
    """
    Stack ADT implimentation
    """
    def __init__(self):
      self.head = Node("head")
      self.size = 0


    # return the items in stack in a more readable format
    def __str__(self):
      curr = self.head.next
      ret = ""
      while curr:
         ret += str(curr.value) + "->"
         curr = curr.next
      return ret[:-3]

    # count total items
    def getlength(self):
      return self.size


    # check if Empty
    def isEmpty(self):
      return self.size == 0


    # returns the last / top elemetn from the adt
    def peek(self):
       # check first if empty
      if self.isEmpty():
         raise Exception("the ADt has no data currently")
      return self.head.next.value


    # insert a value to the ADT
    def push(self, value):
      node = Node(value)
      node.next = self.head.next
      self.head.next = node
      # increment the size of the stack
      self.size += 1



    # delete and return the last element in the statck
    def pop(self):
      if self.isEmpty():
         raise Exception("The ADT is currently Empty")
    # delete last Element
      rem = self.head.next
      self.head.next = self.head.next.next
      # decresse the count
      self.size -= 1
      return rem.value


# request a file
def requestFile():
    """
    A function that request fro a file to read content
    """
    filename = input("Please enter the full file path:  \n")
    try:
        fread = open(filename)
    except Exception as e:
        print(f"File path   {filename}   is not available")
        print(f" Cannot Open the file As it does not exists")
        print("Please provide a coorrect path or full file path")

# exit the program
        exit(1)
    else:
        content = fread.read()
        # print(content)
        return content


# get the content of the file requested

htmlDoc =  requestFile()
c = datetime.datetime.now()
def CheckDocValid(htmlDoc):
    """
    Get all tags from the stack
    """
    s=Stack()
    # get all tags
    z=htmlDoc.replace('<', ' <'); m=z.replace('>', '> ')

    tags=[i for i in m.split() if re.search('<\S+>',i)]
    # get length
    print(len(tags))
    # opening
    btags=[i for i in tags if "/" not in i]
    # closing tags
    ctags=[i for i in tags if "/"  in i]
    # check validation
    for i in htmlDoc.split():
        if i in btags:
            s.push(i)
        elif not s.isEmpty() and (i in ctags) and (i.replace('/','')==s.peek()):
            s.pop()
    # print(tags)
    # print("\n\n")
    # print(btags)
    # print("\n\n")
    # print(ctags)
    # print("\n\n\n\n")
    # print(s)
    return s.isEmpty()


def main():
    print(CheckDocValid(htmlDoc))
    # check time used
    print(f"\n\n  Time used is {datetime.datetime.now()-c}")

main()
