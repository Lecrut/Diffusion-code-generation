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
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    
    result = find_middle(node1)
    print(result)
    
    node_b = ListNode(2)
    node_a = ListNode(1, node_b)
    
    result2 = find_middle(node_a)
    print(result2)
    
    single_node = ListNode(99)
    result3 = find_middle(single_node)
    print(result3)