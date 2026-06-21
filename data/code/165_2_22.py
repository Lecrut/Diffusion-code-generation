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

    def lookup(self, id):
        return self._lookup_recursive(self.root, id)

    def _lookup_recursive(self, node, id):
        if node is None or node.id == id:
            return node
        if id < node.id:
            return self._lookup_recursive(node.left, id)
        else:
            return self._lookup_recursive(node.right, id)
if __name__ == '__main__':
    tree = ContactTree()
    sample_contacts = [{'id': 1, 'name': 'Alice Smith'}, {'id': 2, 'name': 'Bob Johnson'}, {'id': 3, 'name': 'Charlie Brown'}, {'id': 4, 'name': 'David Lee'}]
    for contact in sample_contacts:
        tree.insert(contact['id'], contact['name'])
    print('Contact with id 2:', tree.lookup(2).name)
    tree.delete(2)
    print('Contact with id 2 after deletion:', tree.lookup(2))