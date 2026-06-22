class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def validate_list(head):
    if head is None:
        raise ValueError("Input list is empty")
    current = head
    seen = set()
    while current is not None:
        if id(current) in seen:
            raise ValueError("List contains a cycle")
        seen.add(id(current))
        current = current.next

def find_middle_element(head):
    validate_list(head)
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.value

if __name__ == '__main__':
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    result = find_middle_element(node1)
    print(result)