class Node:

    def __init__(self, value=0, children=None):
        self.value = value
        self.children = children if children is not None else []

    @classmethod
    def is_identical(cls, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.value != node2.value:
            return False
        if len(node1.children) != len(node2.children):
            return False
        for child1, child2 in zip(node1.children, node2.children):
            if not cls.is_identical(child1, child2):
                return False
        return True
if __name__ == '__main__':
    root1 = Node(1)
    root1.children.append(Node(2))
    root1.children.append(Node(3))
    root2 = Node(1)
    root2.children.append(Node(2))
    root2.children.append(Node(3))
    root3 = Node(1)
    root3.children.append(Node(2))
    root3.children.append(Node(4))
    print(Node.is_identical(root1, root2))
    print(Node.is_identical(root1, root3))