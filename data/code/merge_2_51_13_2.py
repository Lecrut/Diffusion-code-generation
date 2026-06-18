class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
def get_head(head_node):
    if head_node is not None:
        return head_node.value
    raise IndexError("List is empty")
if __name__ == '__main__':
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node1.next = node2
    node2.next = node3
    head = get_head(node1)
    print(head)