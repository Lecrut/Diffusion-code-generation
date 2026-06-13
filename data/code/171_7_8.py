class Store:
    def __init__(self, store_id, name):
        self.store_id = store_id
        self.name = name
        self.parent_id = None
        self.children_ids = []
class StoreHierarchy:
    def __init__(self):
        self.stores = {}
    def add_store(self, store):
        self.stores[store.store_id] = store
    def find_store(self, store_id):
        return self.stores.get(store_id)
    def get_all_descendants(self, store_id):
        descendants = []
        queue = [store_id]
        visited = {store_id}
        while queue:
            current_id = queue.pop(0)
            if current_id in self.stores:
                store = self.stores[current_id]
                if current_id != store_id:
                    descendants.append(store)
                for child_id in self.stores[current_id].children_ids:
                    if child_id not in visited:
                        visited.add(child_id)
                        queue.append(child_id)
        return descendants
    def get_direct_parent(self, store_id):
        store = self.find_store(store_id)
        if store and store.parent_id is not None:
            return self.find_store(store.parent_id)
        return None
if __name__ == '__main__':
    hierarchy = StoreHierarchy()
    store1 = Store(1, "HQ")
    store2 = Store(2, "Downtown Branch")
    store3 = Store(3, "North Side")
    store4 = Store(4, "South Side")
    store5 = Store(5, "West End")
    hierarchy.add_store(store1)
    hierarchy.add_store(store2)
    hierarchy.add_store(store3)
    hierarchy.add_store(store4)
    hierarchy.add_store(store5)
    store1.children_ids.extend([2])
    store2.parent_id = 1
    store3.parent_id = 1
    store4.parent_id = 1
    store5.parent_id = 1
    hierarchy.stores[1] = store1
    hierarchy.stores[2] = store2
    hierarchy.stores[3] = store3
    hierarchy.stores[4] = store4
    hierarchy.stores[5] = store5
    print("--- Finding Store by ID (ID 2) ---")
    found_store = hierarchy.find_store(2)
    if found_store:
        print(f"Found: {found_store.name}, Parent ID: {found_store.parent_id}")
    else:
        print("Store not found.")
    print("\n--- Finding Direct Parent of Store 3 (ID 3) ---")
    parent = hierarchy.get_direct_parent(3)
    if parent:
        print(f"Parent Name: {parent.name}, ID: {parent.store_id}")
    else:
        print("No direct parent found.")
    print("\n--- Finding All Descendants of Store 1 (ID 1) ---")
    descendants = hierarchy.get_all_descendants(1)
    if descendants:
        for store in descendants:
            print(f"Descendant: {store.name} (ID: {store.store_id})")
    else:
        print("No descendants found.")