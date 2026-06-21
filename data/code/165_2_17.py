class ContactNode:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None

class ContactTree:
    def __init__(self):
        self.root = None
    
    def insert(self, id, name):
        if not self.root:
            self.root = ContactNode(id, name)
        else:
            self._insert_recursive(self.root, id, name)
    
    def _insert_recursive(self, node, id, name):
        if id < node.id:
            if node.left is None:
                node.left = ContactNode(id, name)
            else:
                self._insert_recursive(node.left, id, name)
        elif id > node.id:
            if node.right is None:
                node.right = ContactNode(id, name)
            else:
                self._insert_recursive(node.right, id, name)
    
    def lookup(self, id):
        return self._lookup_recursive(self.root, id)
    
    def _lookup_recursive(self, node, id):
        if node is None or node.id == id:
            return node
        if id < node.id:
            return self._lookup_recursive(node.left, id)
        else:
            return self._lookup_recursive(node.right, id)
    
    def delete(self, id):
        self.root = self._delete_recursive(self.root, id)
    
    def _delete_recursive(self, node, id):
        if node is None:
            return node
        if id < node.id:
            node.left = self._delete_recursive(node.left, id)
        elif id > node.id:
            node.right = self._delete_recursive(node.right, id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
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
    contact_tree = ContactTree()
    contact_tree.insert(10, "Alice Smith")
    contact_tree.insert(5, "Bob Johnson")
    contact_tree.insert(15, "Charlie Brown")
    contact_tree.insert(7, "David Lee")

    print("Lookup 10:", contact_tree.lookup(10).name)
    print("Lookup 5:", contact_tree.lookup(5).name)

    contact_tree.delete(5)
    print("After deleting 5:")
    if contact_tree.lookup(5) is None:
        print("5 not found")