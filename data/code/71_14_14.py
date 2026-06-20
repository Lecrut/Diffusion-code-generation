class ListNode:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:

    @staticmethod
    def find_middle(head: ListNode) -> int:
        fast = slow = head
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
    middle_value = LinkedList.find_middle(node1)
    print(f'Middle element: {middle_value}')