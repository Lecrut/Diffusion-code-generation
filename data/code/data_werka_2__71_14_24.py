class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

def get_middle_node_value(head):
    if head is None:
        raise ValueError("Linked list cannot be empty")
    
    slow_ptr = head
    fast_ptr = head
    
    while fast_ptr.nxt is not None and fast_ptr.nxt.nxt is not None:
        slow_ptr = slow_ptr.nxt
        fast_ptr = fast_ptr.nxt.nxt
        
    return slow_ptr.val

if __name__ == '__main__':
    n5 = Node(5)
    n4 = Node(4, n5)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    
    result = get_middle_node_value(n1)
    print(result)