class LinkedListNode:

    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:

    @staticmethod
    def find_middle_element(head):
        if not head:
            return None
        slow_pointer = fast_pointer = head
        while fast_pointer and fast_pointer.next_node:
            slow_pointer = slow_pointer.next_node
            fast_pointer = fast_pointer.next_node.next_node
        return slow_pointer.value
if __name__ == '__main__':
    head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4, LinkedListNode(5)))))
    print(f'Middle element of the linked list: {LinkedList.find_middle_element(head)}')