class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst_inorder(root, last_visited=[None]):
    if root:
        if not is_bst_inorder(root.left, last_visited):
            return False
        if last_visited[0] is not None and root.value <= last_visited[0]:
            return False
        last_visited[0] = root.value
        if not is_bst_inorder(root.right, last_visited):
            return False
    return True
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    print(is_bst_inorder(root))