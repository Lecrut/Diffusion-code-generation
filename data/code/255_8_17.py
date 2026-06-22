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
    sample_head = ListNode(1)
    sample_head.next = ListNode(3)
    sample_head.next.next = ListNode(5)
    sample_head.next.next.next = ListNode(7)
    sample_head.next.next.next.next = ListNode(9)
    result = find_maximum(sample_head)
    print(result)