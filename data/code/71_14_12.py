class LinkedList:
    HEAD_MARKER = object()
    TAIL_MARKER = object()

    def __init__(self, values=None):
        self._head = None
        self._size = 0
        if values is not None:
            for val in values:
                self.append(val)

    def append(self, value):
        new_node = self._create_node(value)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current._next is not None:
                current = current._next
            current._next = new_node
        self._size += 1

    def _create_node(self, value):
        node = self.Node(value)
        return node

    class Node:
        def __init__(self, value):
            self._value = value
            self._next = None

        @property
        def value(self):
            return self._value

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self, next_node):
            self._next = next_node

    def get_middle_value(self):
        if self._head is None:
            raise ValueError("List is empty")
        
        slow = self._head
        fast = self._head
        
        while fast._next is not None and fast._next._next is not None:
            slow = slow._next
            fast = fast._next._next
            
        return slow._value

    @property
    def size(self):
        return self._size

if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4, 5])
    print(ll.get_middle_value())
    
    ll2 = LinkedList([1, 2, 3, 4])
    print(ll2.get_middle_value())
    
    ll3 = LinkedList([10])
    print(ll3.get_middle_value())