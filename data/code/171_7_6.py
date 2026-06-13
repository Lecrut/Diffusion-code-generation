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
        if store.store_id not in self.stores:
            self.stores[store.store_id] = store
        else:
            raise ValueError("Store with this ID already exists")
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
    store1 = Store(1, "Flagship Store")
    store2 = Store(2, "Mid-size Outlet")
    store3 = Store(3, "Local Boutique")
    store4 = Store(4, "Small Kiosk")
    store5 = Store(5, "Regional Hub")
    hierarchy.add_store(store1)
    hierarchy.add_store(store2)
    hierarchy.add_store(store3)
    hierarchy.add_store(store4)
    hierarchy.add_store(store5)
    store1.add_child(store2)
    store2.add_child(store3)
    store2.add_child(store4)
    store5.add_child(store1)
    print("--- Store Hierarchy Setup ---")
    def print_hierarchy(start_id):
        target = hierarchy.find_store(start_id)
        if not target:
            print(f"Store ID {start_id} not found.")
            return
        print(f"\nTraversal starting from: {target.name} (ID: {target.store_id})")
        all_stores = []
        queue = [target]
        visited = {target.store_id}
        while queue:
            current = queue.pop(0)
            all_stores.append(current)
            for child in current.children:
                if child.store_id not in visited:
                    visited.add(child.store_id)
                    queue.append(child)
        for store in all_stores:
            parent_name = store.parent.name if store.parent else "ROOT"
            print(f"  ID: {store.store_id}, Name: {store.name}, Parent: {parent_name}")
    print_hierarchy(1)
    print_hierarchy(5)
    print("\n--- Relationship Check (Descendants of Store 1) ---")
    descendants_of_1 = hierarchy.get_all_descendants(1)
    for store in descendants_of_1:
        print(f"Store {store.store_id}: {store.name}")