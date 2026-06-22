class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    MAX_VALUE = float('-inf')

    @staticmethod
    def create_node(value):
        return LinkedList.Node(value)

    @staticmethod
    def is_empty(head):
        return head is None

    def find_maximum(self, head):
        if self.is_empty(head):
            return None
        current = head
        max_val = self.MAX_VALUE
        while current:
            max_val = max(max_val, current.value)
            current = current.next
        return max_val

if __name__ == '__main__':
    linked_list = LinkedList()
    sample_values = [10, 5, 22, 8, 30]
    head = None
    for value in reversed(sample_values):
        new_node = linked_list.create_node(value)
        new_node.next = head
        head = new_node

    max_value = linked_list.find_maximum(head)
    print(max_value)