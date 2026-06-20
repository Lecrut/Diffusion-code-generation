class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle_element(head):
    if not head:
        return None
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value

if __name__ == '__main__':
    list_odd = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    list_even = ListNode(10, ListNode(20, ListNode(30, ListNode(40))))
    list_single = ListNode(99)
    list_empty = None
    
    print(f"Middle element of {list_odd.value}: {find_middle_element(list_odd)}")
    print(f"Middle element of {list_even.value}: {find_middle_element(list_even)}")
    print(f"Middle element of {list_single.value}: {find_middle_element(list_single)}")
    print(f"Middle element of empty list: {find_middle_element(list_empty)}")