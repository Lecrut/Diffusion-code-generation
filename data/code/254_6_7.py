class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def find_min_in_circular_linked_list(head):
    if not head:
        return None
    min_value = head.value
    current = head.next
    while current != head:
        if current.value < min_value:
            min_value = current.value
        current = current.next
    return min_value
if __name__ == '__main__':
    node1 = Node(3)
    node2 = Node(2)
    node3 = Node(5)
    node4 = Node(1)
    node5 = Node(4)
    node6 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node1
    print(find_min_in_circular_linked_list(node1))