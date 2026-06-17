class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    def reverse(self):
        current = self.head
        new_head = None
        while current:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            if current == self.head:
                new_head = current
            current = next_node
        self.head = new_head
if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    print("Original List (Forward):")
    current = dll.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None\n")
    dll.reverse()
    print("Reversed List (Forward):")
    current = dll.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")