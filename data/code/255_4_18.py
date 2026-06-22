class BinarySearchTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_bst(root, value):
    if root is None:
        return BinarySearchTreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

def find_max_in_bst(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.value
if __name__ == '__main__':
    root = BinarySearchTreeNode(5)
    insert_into_bst(root, 3)
    insert_into_bst(root, 7)
    insert_into_bst(root, 2)
    insert_into_bst(root, 4)
    insert_into_bst(root, 8)
    print(find_max_in_bst(root))