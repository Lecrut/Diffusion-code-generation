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
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))
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
    print("Original List:")
    dll.print_list()
    dll.reverse()
    print("Reversed List:")
    dll.print_list()