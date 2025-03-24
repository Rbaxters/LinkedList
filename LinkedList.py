class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Insert at a specific index
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while current_node is not None and position + 1 != index:
                position += 1
                current_node = current_node.next
            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    # Insert at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # Print the linked list
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Create a linked list and insert the names of the people
people_list = LinkedList()

# Insert names at the end of the list
people_names = [
    "Ryan", "Shahood", "Marcos", "Aidan", "Jaiden", 
    "Muntag", "Mason", "Leo", "Chris", "Gavin", "Nate"
]

for name in people_names:
    people_list.insertAtEnd(name)

# Print the names in the linked list
people_list.printList()
