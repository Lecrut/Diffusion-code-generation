class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def find_maximum(head):
    if head is None:
        return None
    max_value = head.value
    current = head.next
    while current:
        if current.value > max_value:
            max_value = current.value
        current = current.next
    return max_value
if __name__ == '__main__':
    head = Node(10)
    head.next = Node(5)
    head.next.next = Node(22)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(30)
    max_value = find_maximum(head)
    print(max_value)