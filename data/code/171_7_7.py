class Store:
    def __init__(self, store_id, name):
        self.store_id = store_id
        self.name = name
        self.parent = None
        self.children = []
    def add_child(self, child_store):
        self.children.append(child_store)
        child_store.parent = self
class StoreHierarchy:
    def __init__(self):
        self.stores = {}
    def add_store(self, store):
        self.stores[store.store_id] = store
    def find_store(self, store_id):
        return self.stores.get(store_id)
    def get_all_descendants(self, store_id):
        descendants = []
        queue = [self.find_store(store_id)]
        visited = {store_id}
        while queue:
            current = queue.pop(0)
            for child in current.children:
                if child.store_id not in visited:
                    descendants.append(child)
                    visited.add(child.store_id)
                    queue.append(child)
        return descendants
if __name__ == '__main__':
    hierarchy = StoreHierarchy()
    store1 = Store(1, "HQ")
    store2 = Store(2, "Store A")
    store3 = Store(3, "Store B")
    store4 = Store(4, "Store C")
    store5 = Store(5, "Store D")
    hierarchy.add_store(store1)
    hierarchy.add_store(store2)
    hierarchy.add_store(store3)
    hierarchy.add_store(store4)
    hierarchy.add_store(store5)
    store1.add_child(store2)
    store2.add_child(store3)
    store2.add_child(store4)
    store3.add_child(store5)
    print("--- Store Hierarchy Data ---")
    for sid, store in hierarchy.stores.items():
        print(f"ID: {store.store_id}, Name: {store.name}")
    print("\n--- Relationship Check (Parent/Child) ---")
    target_id = 2
    found_store = hierarchy.find_store(target_id)
    if found_store:
        print(f"Store ID {target_id} ({found_store.name}) Parent ID: {found_store.parent.store_id if found_store.parent else 'None'}")
    print("\n--- Traversal Check (Descendants of Store 1 - HQ) ---")
    descendants = hierarchy.get_all_descendants(1)
    if descendants:
        for store in descendants:
            print(f"Descendant: ID {store.store_id}, Name: {store.name}")
    else:
        print("No descendants found.")