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
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = self.Node(value)
            else:
                self._insert(node.left, value)
        elif not node.right:
            node.right = self.Node(value)
        else:
            self._insert(node.right, value)

    def find_max(self):
        return self._find_max(self.root).value if self.root else None

    def _find_max(self, node):
        if not node.right:
            return node
        return self._find_max(node.right)
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    print(bst.find_max())