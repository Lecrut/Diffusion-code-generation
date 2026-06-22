class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def get_middle(head):
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
    tail = Node(5)
    n4 = Node(4, tail)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    head = Node(1, n2)
    print(get_middle(head))
    single_node = Node(99)
    print(get_middle(single_node))