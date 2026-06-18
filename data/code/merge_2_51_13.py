class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
def get_head(head_node):
    return head_node if head_node else None
if __name__ == '__main__':
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node1.next = node2
    node2.next = node3
    result = get_head(node1)
    print(result.value if result else None)