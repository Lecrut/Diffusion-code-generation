class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @classmethod
    def is_identical(cls, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return node1.value == node2.value and cls.is_identical(node1.left, node2.left) and cls.is_identical(node1.right, node2.right)
if __name__ == '__main__':
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)
    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)
    tree3.right = TreeNode(4)
    print(TreeNode.is_identical(tree1, tree2))
    print(TreeNode.is_identical(tree1, tree3))