class Item:
    def __init__(self, val):
        self.data = val
        self.parent = None
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self, key):
        self.root = Item(key)
        self.TreeSize = 1

def __del__(self):
    self.delete_tree(self.root)

def print_t(self):
    self.print_tree(self.root)
    print()

def print_tree(self, curr):
    if curr:
        self.print_tree(curr.left_child)
        print(" data -", curr.data, end=" ")
        self.print_tree(curr.right_child)

def insert(self, key):
    curr = self.root
    while curr and curr.data != key:
        if curr.data > key and curr.left_child == None:
            curr.left_child = Item(key)
            curr.left_child.parent = curr
            self.TreeSize += 1
            return
        if curr.data < key and curr.right_child == None:
            curr.right_child = Item(key)
            curr.right_child.parent = curr
            self.TreeSize += 1
            return
        if curr.data > key:
            curr.left_child.parent = curr
            curr = curr.left_child
        else:
            curr.right_child.parent = curr
            curr = curr.right_child

def GreenFunc(self, key):
    curr = self.root
    while curr and curr.data != key:
        if curr.data > key:
            curr.left_child.parent = curr
            curr = curr.left_child
        else:
            curr.right_child.parent = curr
            curr = curr.right_child
    if curr.parent != None and curr.data < curr.parent.data:
        print(curr.parent.data)
    elif curr.parent == None and curr.right_child:
        print(curr.right_child.data)
    elif curr.right_child != None and curr.right_child.data > curr.data or curr.data > curr.parent.data and curr.right_child:
        print(curr.right_child.data)
    elif  curr.right_child == None and curr.data > curr.parent.data:
        while curr.parent != None and curr.parent.data < key:
            if curr.parent:
                curr = curr.parent
        if curr.parent == None:
            print("This item do not have biggest number")
        else:
            print(curr.parent.data)
    else:
        print("This item do not have biggest number")

Tree1 = BinaryTree(9)
insert(Tree1, 6)
insert(Tree1, 6)
insert(Tree1, 3)
insert(Tree1, 14)
insert(Tree1, 7)
insert(Tree1, 8)
insert(Tree1, 12)
insert(Tree1, 15)

print('Please enter the number for search:')
insert = int(input())
print()
print("Nearest item with bigger number - ", end="")
GreenFunc(Tree1, insert)

