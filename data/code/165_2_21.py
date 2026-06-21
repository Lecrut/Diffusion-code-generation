class ContactNode:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None

class ContactTree:
    def __init__(self):
        self.root = None
    
    @staticmethod
    def _insert_recursive(node, id, name):
        if id < node.id:
            if node.left is None:
                node.left = ContactNode(id, name)
            else:
                ContactTree._insert_recursive(node.left, id, name)
        else:
            if node.right is None:
                node.right = ContactNode(id, name)
            else:
                ContactTree._insert_recursive(node.right, id, name)
    
    def insert(self, id, name):
        if not self.root:
            self.root = ContactNode(id, name)
        else:
            ContactTree._insert_recursive(self.root, id, name)
    
    @staticmethod
    def _search_recursive(node, id):
        if node is None or node.id == id:
            return node
        if id < node.id:
            return ContactTree._search_recursive(node.left, id)
        return ContactTree._search_recursive(node.right, id)
    
    def search(self, id):
        return ContactTree._search_recursive(self.root, id)
    
    @staticmethod
    def _delete_recursive(node, id):
        if node is None:
            return node
        if id < node.id:
            node.left = ContactTree._delete_recursive(node.left, id)
        elif id > node.id:
            node.right = ContactTree._delete_recursive(node.right, id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = ContactTree._min_value_node(node.right)
            node.id = temp.id
            node.name = temp.name
            node.right = ContactTree._delete_recursive(node.right, temp.id)
        return node
    
    def delete(self, id):
        self.root = ContactTree._delete_recursive(self.root, id)
    
    @staticmethod
    def _min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

if __name__ == '__main__':
    contact_tree = ContactTree()
    contact_tree.insert(10, 'Alice Smith')
    contact_tree.insert(5, 'Bob Johnson')
    contact_tree.insert(15, 'Charlie Brown')
    
    print("Search for ID 10:", contact_tree.search(10).name)
    print("Delete ID 5")
    contact_tree.delete(5)
    print("Search for ID 5 after deletion:", contact_tree.search(5))