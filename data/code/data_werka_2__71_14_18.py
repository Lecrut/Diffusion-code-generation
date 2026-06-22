class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

def get_middle_value(head):
    if head is None:
        raise ValueError("List is empty")
    
    current_slow = head
    current_fast = head
    
    while current_fast.next is not None and current_fast.next.next is not None:
        current_fast = current_fast.next.next
        current_slow = current_slow.next
        
    return current_slow.val

if __name__ == '__main__':
    tail = Node(5)
    n4 = Node(4, tail)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    
    result = get_middle_value(n1)
    print(result)