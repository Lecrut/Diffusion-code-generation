class ListNode:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle_element(head: ListNode) -> int:
    if not head:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value
if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(f'Middle element: {find_middle_element(node1)}')
    empty_head = None
    print(f'Middle element of empty list: {find_middle_element(empty_head)}')