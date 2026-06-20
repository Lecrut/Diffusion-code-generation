class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(root, prev=float('-inf')):
    if not root:
        return True
    if not is_valid_bst(root.left, prev):
        return False
    if root.value <= prev:
        return False
    prev = root.value
    return is_valid_bst(root.right, prev)
if __name__ == '__main__':
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    print(is_valid_bst(tree))