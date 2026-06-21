class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    EMPTY_LIST_ERROR = 'List is empty'

    @staticmethod
    def _get_node_by_index(head, index):
        current = head
        for _ in range(index):
            if not current:
                raise IndexError('Index out of range')
            current = current.next
        return current

    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            last = self._get_node_by_index(self.head, -1)
            last.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, index):
        if not self.head:
            raise ValueError(LinkedList.EMPTY_LIST_ERROR)
        if index == 0:
            self.head = self.head.next
            return
        previous = self._get_node_by_index(self.head, index - 1)
        current = previous.next
        previous.next = current.next
        current = None

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.prepend(0)
    print(linked_list.search(1))
    print(linked_list.search(3))
    linked_list.delete(1)
    print(linked_list.search(2))