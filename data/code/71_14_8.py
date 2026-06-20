class ListNode:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle_element(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value if slow else None
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
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node6.next = node7
    node7.next = node8
    node8.next = node9
    print(f'Middle element of the first list: {find_middle_element(node1)}')
    print(f'Middle element of the second list: {find_middle_element(node6)}')