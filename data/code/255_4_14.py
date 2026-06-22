class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    elif value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    return root

def find_max_element(node):
    if node is None:
        raise ValueError('Empty tree has no maximum element')
    current_node = node
    while current_node.right:
        current_node = current_node.right
    return current_node.value
if __name__ == '__main__':
    root = TreeNode(10)
    insert_node(root, 5)
    insert_node(root, 20)
    insert_node(root, 3)
    insert_node(root, 7)
    print(find_max_element(root))
    root_empty = None
    try:
        print(find_max_element(root_empty))
    except ValueError as e:
        print(e)