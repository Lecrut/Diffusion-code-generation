class BinarySearchTree:

    def __init__(self):
        self.root = None

    class Node:

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def insert(self, value):
        if not self.root:
            self.root = self.Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = self.Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if not node.right:
                node.right = self.Node(value)
            else:
                self._insert_recursive(node.right, value)

    def find_max(self):
        if not self.root:
            raise ValueError('Empty tree')
        return self._find_max_recursive(self.root).value

    def _find_max_recursive(self, node):
        while node.right:
            node = node.right
        return node
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(15)
    bst.insert(20)
    print(bst.find_max())