class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_max_element(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.value
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3, left=TreeNode(2), right=TreeNode(4))
    root.right = TreeNode(7, left=TreeNode(6))
    print(find_max_element(root))