class Node:
    def __init__(self, data):
        self.data = data
        self.under = None

class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
        else:
            new_node.under = self.top
            self.top = new_node

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            print("STACK IS EMPTY")
        else:
            popped = self.top
            self.top = self.top.under
            print(f"you have popped, {popped.data}")
        
    def peak(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print(self.top.data)

    def display(self):
        items = []
        current = stack.top
        while current != None:
            items.append(current.data)
            current = current.under
        for item in items:
            print(item)
 
stack = Stack()
run = True
while run:
    choice = int(input("1(push), 2(pop), 3(is empty?), 4(peak), 5(display), 6(quit)"))
    if type(choice) != int:
        print("enter a number")
    else:
        print("LOADING....")
        if choice == 1:
            data = int(input("Enter data to push: "))
            stack.push(data)
        if choice == 2:
            stack.pop()
        if choice == 3:
            if stack.is_empty():
                print("STACK IS EMPTY")
            else:
                print("STACK IS NOT EMPTY")
        if choice == 4:
            stack.peak()
        if choice == 5:
            stack.display()
        if choice == 6:
            run = False
        

