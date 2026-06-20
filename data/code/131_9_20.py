class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(root):
    stack = []
    prev = None
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        if prev and node.value <= prev.value:
            return False
        prev = node
        root = node.right
    return True
if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(is_valid_bst(root))