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
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    print(find_max_element(root))