class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def find_minimum(head):
    if head is None or head.next == head:
        return head.value if head else None
    current = head
    minimum = current.value
    while current.next != head:
        current = current.next
        if current.value < minimum:
            minimum = current.value
    return minimum
if __name__ == '__main__':
    node1 = Node(3)
    node2 = Node(5)
    node3 = Node(2)
    node4 = Node(8)
    node5 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node1
    print('Minimum value in circular linked list:', find_minimum(node1))