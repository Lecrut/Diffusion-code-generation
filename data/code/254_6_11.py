class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def find_min_value(head):
    if not head:
        return None
    min_val = head.value
    current = head.next
    while current != head:
        if current.value < min_val:
            min_val = current.value
        current = current.next
    return min_val
if __name__ == '__main__':
    node1 = Node(3)
    node2 = Node(4)
    node3 = Node(1)
    node4 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1
    print(find_min_value(node1))