class ListNode:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_maximum(head):
    if not head:
        return None
    max_value = head.value
    current = head.next
    while current:
        if current.value > max_value:
            max_value = current.value
        current = current.next
    return max_value
if __name__ == '__main__':
    head = ListNode(10)
    head.next = ListNode(5)
    head.next.next = ListNode(22)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(30)
    result = find_maximum(head)
    print(result)