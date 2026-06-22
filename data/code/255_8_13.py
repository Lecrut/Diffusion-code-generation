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
    node1 = ListNode(3)
    node2 = ListNode(5, node1)
    node3 = ListNode(8, node2)
    head = node3
    print(find_max_element(head))