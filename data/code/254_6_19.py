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
    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(4)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head
    min_value = find_min_in_circular_linked_list(head)
    print(min_value)