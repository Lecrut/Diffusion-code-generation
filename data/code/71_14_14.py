class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def get_middle_value(head):
    if head is None:
        raise ValueError("List is empty")
    
    slow = head
    fast = head
    
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    return slow.value

if __name__ == '__main__':
    node4 = Node(4)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    
    result = get_middle_value(node1)
    print(result)