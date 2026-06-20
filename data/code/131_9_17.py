class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst(node, low=float('-inf'), high=float('inf')):
    if not node:
        return True
    if not low < node.value < high:
        return False
    return is_bst(node.left, low, node.value) and is_bst(node.right, node.value, high)
if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(is_bst(root))