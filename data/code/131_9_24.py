class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst_inorder(node, prev_val=float('-inf')):
    if node is None:
        return True
    if not is_bst_inorder(node.left, prev_val):
        return False
    if node.value <= prev_val:
        return False
    prev_val = node.value
    return is_bst_inorder(node.right, prev_val)
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    is_valid_bst = is_bst_inorder(root)
    print(is_valid_bst)