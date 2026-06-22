class CircularLinkedList:

    def __init__(self, value):
        self.value = value
        self.next = None

def find_minimum(head):
    if head is None or head.next == head:
        return head.value
    current = head
    minimum = current.value
    while True:
        if current.value < minimum:
            minimum = current.value
        current = current.next
        if current == head:
            break
    return minimum
if __name__ == '__main__':
    node1 = CircularLinkedList(5)
    node2 = CircularLinkedList(2)
    node3 = CircularLinkedList(8)
    node4 = CircularLinkedList(1)
    node5 = CircularLinkedList(9)
    node6 = CircularLinkedList(3)
    node7 = CircularLinkedList(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node1
    minimum_value = find_minimum(node1)
    print(minimum_value)