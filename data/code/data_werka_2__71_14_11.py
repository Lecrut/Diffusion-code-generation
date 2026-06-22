class LinkNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def middle_node_value(head):
    if head is None:
        return None
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.data

if __name__ == '__main__':
    head = LinkNode(1, LinkNode(2, LinkNode(3, LinkNode(4, LinkNode(5)))))
    result = middle_node_value(head)
    print(result)