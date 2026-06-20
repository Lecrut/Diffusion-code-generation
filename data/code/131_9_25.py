class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(root, lower=float('-inf'), upper=float('inf')):
    if not root:
        return True
    if not lower < root.value < upper:
        return False
    return is_valid_bst(root.left, lower, root.value) and is_valid_bst(root.right, root.value, upper)

def in_order_traversal(node):
    result = []

    def traverse(current_node):
        if current_node:
            traverse(current_node.left)
            result.append(current_node.value)
            traverse(current_node.right)
    traverse(node)
    return result
if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15, TreeNode(6), TreeNode(20))
    is_bst = is_valid_bst(root)
    print('Is Valid BST:', is_bst)
    in_order_result = in_order_traversal(root)
    print('In-order Traversal:', in_order_result)