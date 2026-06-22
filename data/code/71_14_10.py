class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_middle_value(head):
    if head is None:
        raise ValueError("List is empty")
    
    current_slow = head
    current_fast = head
    
    while current_fast.next is not None and current_fast.next.next is not None:
        current_fast = current_fast.next.next
        current_slow = current_slow.next
        
    return current_slow.data

if __name__ == '__main__':
    h = Node(10)
    h.next = Node(20)
    h.next.next = Node(30)
    h.next.next.next = Node(40)
    h.next.next.next.next = Node(50)
    
    print(get_middle_value(h))