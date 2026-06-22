class CircularLinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

def find_minimum_in_circular_linked_list(head):
    if not head:
        return None
    current = head
    minimum_value = current.value
    while True:
        if current.value < minimum_value:
            minimum_value = current.value
        current = current.next
        if current == head:
            break
    return minimum_value
if __name__ == '__main__':
    node1 = CircularLinkedListNode(5)
    node2 = CircularLinkedListNode(2)
    node3 = CircularLinkedListNode(8)
    node4 = CircularLinkedListNode(1)
    node5 = CircularLinkedListNode(9)
    node6 = CircularLinkedListNode(3)
    node7 = CircularLinkedListNode(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node1
    min_value = find_minimum_in_circular_linked_list(node1)
    print(min_value)