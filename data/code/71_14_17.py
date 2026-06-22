class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    if head is None:
        raise ValueError("List is empty")
    
    slow = head
    fast = head
    
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    return slow.val

if __name__ == '__main__':
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    
    result = find_middle(n1)
    print(result)
    
    n2_even = ListNode(2)
    n1_even = ListNode(1, n2_even)
    
    result_even = find_middle(n1_even)
    print(result_even)