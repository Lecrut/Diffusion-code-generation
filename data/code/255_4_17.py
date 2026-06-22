class BinarySearchTree:

    def __init__(self):
        self.root = None

    class Node:

        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

    def insert(self, key):
        if self.root is None:
            self.root = self.Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = self.Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = self.Node(key)
            else:
                self._insert_recursive(node.right, key)

    def find_max(self):
        if self.root is None:
            return None
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.val
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    print(bst.find_max())