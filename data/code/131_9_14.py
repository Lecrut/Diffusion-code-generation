class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst(node):
    stack = []
    prev = None
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if prev and node.value <= prev.value:
            return False
        prev = node
        node = node.right
    return True
if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(is_bst(root))