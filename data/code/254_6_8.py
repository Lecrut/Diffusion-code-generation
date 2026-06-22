class CircularLinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

def find_minimum(head):
    if not head or not head.next:
        return None
    current = head
    minimum_value = current.value
    while current.next != head:
        if current.next.value < minimum_value:
            minimum_value = current.next.value
        current = current.next
    return minimum_value
if __name__ == '__main__':
    head = CircularLinkedListNode(5)
    node2 = CircularLinkedListNode(2)
    node3 = CircularLinkedListNode(8)
    node4 = CircularLinkedListNode(1)
    node5 = CircularLinkedListNode(9)
    node6 = CircularLinkedListNode(3)
    node7 = CircularLinkedListNode(7)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = head
    minimum_value = find_minimum(head)
    print(minimum_value)