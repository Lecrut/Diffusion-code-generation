class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_middle(head):
    if head is None:
        raise ValueError("List is empty")
    
    slow_ptr = head
    fast_ptr = head
    
    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        if fast_ptr is None:
            break
        slow_ptr = slow_ptr.next
        
    return slow_ptr.value

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    
    result = get_middle(n1)
    print(result)