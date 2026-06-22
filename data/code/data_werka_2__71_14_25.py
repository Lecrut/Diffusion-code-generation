class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_middle_element(head):
    if head is None:
        raise ValueError("List is empty")
    slow_pointer = head
    fast_pointer = head
    while fast_pointer.next is not None and fast_pointer.next.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return slow_pointer.value

if __name__ == '__main__':
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)
    node3 = LinkedListNode(3)
    node4 = LinkedListNode(4)
    node5 = LinkedListNode(5)
    node6 = LinkedListNode(6)
    node7 = LinkedListNode(7)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    
    middle_value = get_middle_element(node1)
    print(middle_value)
    
    single_node = LinkedListNode(42)
    single_middle = get_middle_element(single_node)
    print(single_middle)