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
    head = ListNode(1)
    current = head
    for value in [2, 3, 4, 5, 6]:
        current.next = ListNode(value)
        current = current.next
    middle_value = find_middle_element(head)
    print(f'Middle element of linked list: {middle_value}')