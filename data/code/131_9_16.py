class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def in_order_traversal(node):
    result = []
    if node is not None:
        result.extend(in_order_traversal(node.left))
        result.append(node.value)
        result.extend(in_order_traversal(node.right))
    return result

def is_valid_bst(root):
    values = in_order_traversal(root)
    for i in range(1, len(values)):
        if values[i] <= values[i - 1]:
            return False
    return True
if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    print(is_valid_bst(root))