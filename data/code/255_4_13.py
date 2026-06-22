class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_max_element(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.value
if __name__ == '__main__':
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(15)
    tree.right.left = TreeNode(12)
    tree.right.right = TreeNode(20)
    max_value = find_max_element(tree)
    print(max_value)