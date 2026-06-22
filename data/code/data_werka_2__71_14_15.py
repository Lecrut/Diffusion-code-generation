class Node:
    def __init__(self, value: int, next_node: 'Node' = None):
        self.value = value
        self.next = next_node

def get_middle_value(head: Node) -> int:
    if head is None:
        raise ValueError("List is empty")
    if head.next is None:
        return head.value
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.value

if __name__ == '__main__':
    h = Node(10)
    h.next = Node(20)
    h.next.next = Node(30)
    h.next.next.next = Node(40)
    result = get_middle_value(h)
    print(result)