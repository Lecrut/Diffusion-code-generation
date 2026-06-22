class Node:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_maximum(head):
    if not head:
        return None
    max_value = float('-inf')
    current = head
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
    result = find_maximum(head)
    print(result)