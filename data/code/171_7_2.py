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
    def get_parent(self, store_id):
        store = self.find_store(store_id)
        if store and store.parent_id is not None:
            return self.find_store(store.parent_id)
        return None
def build_hierarchy():
    hierarchy = StoreHierarchy()
    stores_data = [
        (1, "HQ Store"),
        (2, "Downtown Branch"),
        (3, "North Side Outlet"),
        (4, "South Side Location"),
        (5, "West End Retail")
    ]
    for store_id, name in stores_data:
        store = Store(store_id, name)
        hierarchy.add_store(store)
    hierarchy.stores[1].children_ids = [2, 3]
    hierarchy.stores[2].parent_id = 1
    hierarchy.stores[3].parent_id = 1
    hierarchy.stores[4].parent_id = 1
    hierarchy.stores[5].parent_id = 1
    return hierarchy
if __name__ == '__main__':
    store_hierarchy = build_hierarchy()
    print("--- Store Hierarchy Data ---")
    for store_id, store in sorted(store_hierarchy.stores.items()):
        parent = store_hierarchy.get_parent(store_id)
        print(f"ID: {store.store_id}, Name: {store.name}, Parent ID: {store.parent_id}")
    print("\n--- Traversal Example (Descendants of HQ Store - ID 1) ---")
    hq_store = store_hierarchy.find_store(1)
    if hq_store:
        descendants = store_hierarchy.get_all_descendants(1)
        for store in descendants:
            print(f"Descendant: {store.name} (ID: {store.store_id})")
    else:
        print("HQ Store not found.")
    print("\n--- Relationship Check Example (Parent of Downtown Branch - ID 2) ---")
    downtown_branch = store_hierarchy.find_store(2)
    if downtown_branch:
        parent = store_hierarchy.get_parent(2)
        if parent:
            print(f"Parent of {downtown_branch.name} is: {parent.name} (ID: {parent.store_id})")
        else:
            print(f"{downtown_branch.name} has no recorded parent.")
    else:
        print("Downtown Branch not found.")