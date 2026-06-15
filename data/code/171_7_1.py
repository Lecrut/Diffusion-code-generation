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
    store4.add_child(store5)
    print("--- Store Hierarchy Setup ---")
    def print_store_details(store):
        print(f"ID: {store.store_id}, Name: {store.name}")
    print_store_details(store1)
    print_store_details(store2)
    print_store_details(store3)
    print_store_details(store4)
    print_store_details(store5)
    print("\n--- Relationship Check: Parent/Child ---")
    target_id = 2
    found_store = hierarchy.find_store(target_id)
    if found_store:
        print(f"Store {target_id} ({found_store.name}) has parent ID: {found_store.parent.store_id}")
    print("\n--- Relationship Check: Descendants ---")
    start_id = 1
    descendants = hierarchy.get_all_descendants(start_id)
    print(f"All descendants of Store {start_id} ({hierarchy.find_store(start_id).name}):")
    for store in descendants:
        print(f"- ID: {store.store_id}, Name: {store.name}")