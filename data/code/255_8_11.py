class ListNode:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_maximum(head):
    if not head:
        return None
    max_value = float('-inf')
    current = head
    while current:
        max_value = max(max_value, current.value)
        current = current.next
    return max_value
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(7)
    result = find_maximum(head)
    print(result)