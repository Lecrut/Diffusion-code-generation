class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    stack = []
    prev = float('-inf')
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        if node.value <= prev:
            return False
        prev = node.value
        root = node.right
    return True
if __name__ == '__main__':
    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    print(is_valid_bst(tree))