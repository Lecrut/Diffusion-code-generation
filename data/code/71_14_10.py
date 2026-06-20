class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    @staticmethod
    def create_list(values):
        dummy_head = ListNode()
        current = dummy_head
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy_head.next

    @staticmethod
    def find_middle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

if __name__ == '__main__':
    list_odd = LinkedList.create_list([1, 2, 3, 4, 5])
    list_even = LinkedList.create_list([10, 20, 30, 40])
    list_single = LinkedList.create_list([99])
    list_empty = None

    print(f"Middle element of {list_odd}: {LinkedList.find_middle(list_odd)}")
    print(f"Middle element of {list_even}: {LinkedList.find_middle(list_even)}")
    print(f"Middle element of {list_single}: {LinkedList.find_middle(list_single)}")
    print(f"Middle element of {list_empty}: {LinkedList.find_middle(list_empty)}")