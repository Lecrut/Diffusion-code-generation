class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def find_minimum(head):
    if not head:
        return None
    current_min = head.value
    current = head.next
    while current != head:
        if current.value < current_min:
            current_min = current.value
        current = current.next
    return current_min
if __name__ == '__main__':
    head = Node(5)
    node2 = Node(2)
    node3 = Node(8)
    node4 = Node(1)
    node5 = Node(9)
    node6 = Node(3)
    node7 = Node(7)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = head
    print(find_minimum(head))