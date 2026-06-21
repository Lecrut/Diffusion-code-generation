class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        if not isinstance(value, int):
            raise ValueError('Value must be an integer')
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, value):
        if not isinstance(value, int):
            raise ValueError('Value must be an integer')
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        if not isinstance(value, int):
            raise ValueError('Value must be an integer')
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def search(self, value):
        if not isinstance(value, int):
            raise ValueError('Value must be an integer')
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
if __name__ == '__main__':
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    print(ll.search(10))
    print(ll.search(30))
    print(ll.delete(20))
    print(ll.search(20))