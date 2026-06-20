class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    stack = []
    prev_value = float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        if node.value <= prev_value:
            return False
        prev_value = node.value
        root = node.right
    return True
if __name__ == '__main__':
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    print(is_valid_bst(tree))