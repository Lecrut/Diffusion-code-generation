class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def get_middle_element(head):
    if head is None:
        raise ValueError("List is empty")
    slow_ptr = head
    fast_ptr = head
    while fast_ptr.next is not None and fast_ptr.next.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr.value

if __name__ == '__main__':
    node_9 = Node(9)
    node_8 = Node(8, node_9)
    node_7 = Node(7, node_8)
    node_6 = Node(6, node_7)
    node_5 = Node(5, node_6)
    node_4 = Node(4, node_5)
    node_3 = Node(3, node_4)
    node_2 = Node(2, node_3)
    node_1 = Node(1, node_2)
    result = get_middle_element(node_1)
    print(result)