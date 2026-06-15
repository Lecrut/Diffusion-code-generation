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
    store3 = Store(3, "Suburb Outlet")
    store4 = Store(4, "Westside Location")
    store5 = Store(5, "Eastside Retail")
    hierarchy.add_store(store1)
    hierarchy.add_store(store2)
    hierarchy.add_store(store3)
    hierarchy.add_store(store4)
    hierarchy.add_store(store5)
    store1.children_ids = [2]
    store2.parent_id = 1
    store2.children_ids = [3]
    store3.parent_id = 2
    store3.children_ids = [4]
    store4.parent_id = 3
    store5.parent_id = 1
    print("--- Store Hierarchy Data ---")
    for store_id, store in hierarchy.stores.items():
        print(f"ID: {store.store_id}, Name: {store.name}, Parent ID: {store.parent_id}")
    print("\n--- Traversal Examples ---")
    target_id = 1
    print(f"\nDirect Children of Store {target_id} (HQ):")
    direct_children = hierarchy.get_direct_children(target_id)
    for child in direct_children:
        print(f"- {child.name} (ID: {child.store_id})")
    target_id = 1
    print(f"\nAll Descendants of Store {target_id} (HQ):")
    descendants = hierarchy.get_all_descendants(target_id)
    for descendant in descendants:
        print(f"- {descendant.name} (ID: {descendant.store_id})")
    target_id = 3
    print(f"\nDirect Children of Store {target_id} (Suburb Outlet):")
    direct_children = hierarchy.get_direct_children(target_id)
    for child in direct_children:
        print(f"- {child.name} (ID: {child.store_id})")