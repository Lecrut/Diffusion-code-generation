class Node:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None

class ContactBST:

    def __init__(self):
        self.root = None

    def insert(self, id, name):
        if not self.root:
            self.root = Node(id, name)
        else:
            self._insert_recursive(self.root, id, name)

    def _insert_recursive(self, node, id, name):
        if id < node.id:
            if node.left is None:
                node.left = Node(id, name)
            else:
                self._insert_recursive(node.left, id, name)
        elif id > node.id:
            if node.right is None:
                node.right = Node(id, name)
            else:
                self._insert_recursive(node.right, id, name)

    def lookup(self, id):
        return self._lookup_recursive(self.root, id)

    def _lookup_recursive(self, node, id):
        if not node or node.id == id:
            return node
        if id < node.id:
            return self._lookup_recursive(node.left, id)
        else:
            return self._lookup_recursive(node.right, id)

    def delete(self, id):
        self.root = self._delete_recursive(self.root, id)

    def _delete_recursive(self, node, id):
        if not node:
            return node
        if id < node.id:
            node.left = self._delete_recursive(node.left, id)
        elif id > node.id:
            node.right = self._delete_recursive(node.right, id)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.id = temp.id
            node.name = temp.name
            node.right = self._delete_recursive(node.right, temp.id)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
if __name__ == '__main__':
    bst = ContactBST()
    bst.insert(10, 'Alice')
    bst.insert(5, 'Bob')
    bst.insert(15, 'Charlie')
    print(bst.lookup(10).name)
    bst.delete(10)
    print(bst.lookup(10))