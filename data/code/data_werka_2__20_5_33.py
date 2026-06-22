class Node:

    def __init__(self, data):
        self.data = data
        self.children = []

    @classmethod
    def is_identical(cls, node1, node2):
        if not isinstance(node1, cls) or not isinstance(node2, cls):
            return False
        if node1.data != node2.data:
            return False
        if len(node1.children) != len(node2.children):
            return False
        for child1, child2 in zip(node1.children, node2.children):
            if not cls.is_identical(child1, child2):
                return False
        return True
if __name__ == '__main__':
    root1 = Node(1)
    child1_1 = Node(2)
    child1_2 = Node(3)
    root1.children.append(child1_1)
    root1.children.append(child1_2)
    root2 = Node(1)
    child2_1 = Node(2)
    child2_2 = Node(3)
    root2.children.append(child2_1)
    root2.children.append(child2_2)
    root3 = Node(1)
    child3_1 = Node(2)
    child3_2 = Node(4)
    root3.children.append(child3_1)
    root3.children.append(child3_2)
    print(Node.is_identical(root1, root2))
    print(Node.is_identical(root1, root3))