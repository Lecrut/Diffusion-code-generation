class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif node.right is None:
            node.right = Node(value)
        else:
            self._insert_recursive(node.right, value)

    def find_max(self):
        return self._find_max_recursive(self.root).value

    def _find_max_recursive(self, node):
        current = node
        while current.right:
            current = current.right
        return current

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
if __name__ == '__main__':
    bst1 = BinarySearchTree()
    bst1.insert(5)
    bst1.insert(3)
    bst1.insert(7)
    bst1.insert(2)
    bst1.insert(4)
    bst1.insert(6)
    bst1.insert(8)
    print(bst1.find_max())
    bst2 = BinarySearchTree()
    bst2.insert(10)
    bst2.insert(5)
    bst2.insert(15)
    bst2.insert(3)
    bst2.insert(7)
    bst2.insert(12)
    bst2.insert(18)
    print(bst2.find_max())