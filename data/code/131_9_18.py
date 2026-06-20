class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst(node, prev_val=float('-inf')):
    if node is None:
        return True
    if not is_bst(node.left, prev_val):
        return False
    if node.value <= prev_val:
        raise ValueError("BST property violated")
    prev_val = node.value
    if not is_bst(node.right, prev_val):
        return False
    return True

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    try:
        result = is_bst(root)
        print("Is valid BST:", result)
    except ValueError as e:
        print(e)