class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def get_middle(head):
    if head is None:
        raise ValueError("List is empty")
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.val

def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head

if __name__ == '__main__':
    lookup = {
        "odd": [1, 2, 3, 4, 5],
        "even": [10, 20, 30, 40],
        "single": [99]
    }
    for name, vals in lookup.items():
        head = build_list(vals)
        mid_val = get_middle(head)
        print(mid_val)