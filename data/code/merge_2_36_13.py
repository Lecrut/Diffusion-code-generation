class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class OptimizedBST:
    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        height_left = 1 + (self.get_height(root.left)) if root.left else 0
        height_right = 1 + (self.get_height(root.right)) if root.right else 0
        balance_factor = height_left - height_right
        if balance_factor > 1:
            if key < root.key:
                return self.rotateRight(root)
            else:
                temp = Node(key)
                temp.left, temp.right = root.left, root
                return self.rotateLeft(temp)
        elif balance_factor < -1:
            if key > root.key:
                return self.rotateLeft(root)
            else:
                temp = Node(key)
                temp.left, temp.right = root, root.right
                return self.rotateRight(temp)
        return root
    def get_height(self, node):
        if not node:
            return 0
        h_left = self.get_height(node.left)
        h_right = self.get_height(node.right)
        return max(h_left, h_right) + 1
    def rotateRight(self, z):
        y = z.left
        T2 = y.right
        y.right = z
        z.left = T2
        return y
    def rotateLeft(self, z):
        y = z.right
        T3 = y.left
        y.left = z
        z.right = T3
        return y
def build_tree(values):
    root = None
    for val in values:
        root = OptimizedBST().insert(root, val)
    return root
if __name__ == '__main__':
    sample_data = [50, 30, 20, 40, 70, 60, 80]
    tree_root = build_tree(sample_data)
    def inorder_traversal(node):
        if not node:
            return []
        left_list = inorder_traversal(node.left)
        right_list = inorder_traversal(node.right)
        return left_list + [node.key] + right_list
    result_order = inorder_traversal(tree_root)
    print(result_order)