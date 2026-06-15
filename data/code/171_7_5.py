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
    def get_direct_children(self, store_id):
        store = self.find_store(store_id)
        if store:
            return [self.stores[cid] for cid in store.children_ids if cid in self.stores]
        return []
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
    store1.parent_id = None
    store2.parent_id = 1
    store3.parent_id = 1
    store4.parent_id = 1
    store5.parent_id = 1
    store1.children_ids = [2, 3, 4]
    store2.children_ids = []
    store3.children_ids = []
    store4.children_ids = []
    store5.children_ids = []
    print("--- Finding Store by ID (ID 1) ---")
    found_store = hierarchy.find_store(1)
    if found_store:
        print(f"Store Found: {found_store.name}, Parent ID: {found_store.parent_id}")
    print("\n--- Finding Store by ID (ID 2) ---")
    found_store = hierarchy.find_store(2)
    if found_store:
        print(f"Store Found: {found_store.name}, Parent ID: {found_store.parent_id}")
    print("\n--- Finding Direct Children of Store 1 (HQ) ---")
    children = hierarchy.get_direct_children(1)
    for child in children:
        print(f"Child: {child.name} (ID: {child.store_id})")
    print("\n--- Finding All Descendants of Store 1 (HQ) ---")
    descendants = hierarchy.get_all_descendants(1)
    for descendant in descendants:
        print(f"Descendant: {descendant.name} (ID: {descendant.store_id})")