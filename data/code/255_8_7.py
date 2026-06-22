class ListNode:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_max_element(head):
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
    head = ListNode(3)
    head.next = ListNode(5)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(1)
    max_element = find_max_element(head)
    print(max_element)