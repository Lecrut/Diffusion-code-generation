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
            if current_id != store_id:
                store = self.find_store(current_id)
                if store:
                    descendants.append(store)
            for child_id in self.stores[current_id].children_ids:
                if child_id not in visited:
                    visited.add(child_id)
                    queue.append(child_id)
        return descendants
    def get_direct_children(self, store_id):
        store = self.find_store(store_id)
        if store:
            return [self.find_store(cid) for cid in store.children_ids if self.find_store(cid)]
        return []
def build_hierarchy():
    hierarchy = StoreHierarchy()
    stores_data = [
        {"id": 1, "name": "HQ Store"},
        {"id": 2, "name": "Downtown Branch"},
        {"id": 3, "name": "North Substore"},
        {"id": 4, "name": "South Substore"},
        {"id": 5, "name": "West Outlet"},
        {"id": 6, "name": "East Outlet"}
    ]
    for data in stores_data:
        store = Store(data["id"], data["name"])
        hierarchy.add_store(store)
    hierarchy.stores[1].children_ids = [2, 3, 6]
    hierarchy.stores[2].parent_id = 1
    hierarchy.stores[3].parent_id = 1
    hierarchy.stores[4].parent_id = 2
    hierarchy.stores[5].parent_id = 3
    hierarchy.stores[6].parent_id = 1
    return hierarchy
if __name__ == '__main__':
    store_hierarchy = build_hierarchy()
    print("--- Store Hierarchy Data ---")
    for store_id, store in sorted(store_hierarchy.stores.items()):
        print(f"ID: {store.store_id}, Name: {store.name}, Parent ID: {store.parent_id}, Children IDs: {store.children_ids}")
    print("\n--- Relationship Checking Examples ---")
    target_id = 4
    found_store = store_hierarchy.find_store(target_id)
    print(f"Finding Store ID {target_id}: {found_store}")
    hq_id = 1
    direct_children = store_hierarchy.get_direct_children(hq_id)
    print(f"\nDirect Children of HQ ({hq_id}):")
    for child in direct_children:
        print(f"- {child.name} (ID: {child.store_id})")
    downtown_id = 2
    descendants = store_hierarchy.get_all_descendants(downtown_id)
    print(f"\nAll Descendants of Downtown Branch ({downtown_id}):")
    for descendant in descendants:
        print(f"- {descendant.name} (ID: {descendant.store_id})")
    west_outlet_id = 5
    west_outlet = store_hierarchy.find_store(west_outlet_id)
    if west_outlet:
        print(f"\nDetails for West Outlet ({west_outlet_id}):")
        print(f"Parent is {store_hierarchy.find_store(west_outlet.parent_id).name}")