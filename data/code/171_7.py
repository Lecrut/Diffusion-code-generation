class Store:
    def __init__(self, store_id, name):
        self.store_id = store_id
        self.name = name
        self.parent = None
        self.children = []
class StoreHierarchy:
    def __init__(self):
        self.stores = {}
    def add_store(self, store):
        self.stores[store.store_id] = store
    def build_hierarchy(self, store_list):
        for store in store_list:
            if store.store_id not in self.stores:
                self.add_store(store)
            else:
                pass
    def find_store(self, store_id):
        return self.stores.get(store_id)
    def get_all_descendants(self, store_id):
        descendants = []
        queue = [store_id]
        visited = {store_id}
        while queue:
            current_id = queue.pop(0)
            current_store = self.find_store(current_id)
            if current_store:
                descendants.append(current_store)
                for child in current_store.children:
                    if child.store_id not in visited:
                        visited.add(child.store_id)
                        queue.append(child.store_id)
        return descendants
if __name__ == '__main__':
    hierarchy = StoreHierarchy()
    stores_data = [
        {"id": 1, "name": "HQ Store"},
        {"id": 2, "name": "Branch A"},
        {"id": 3, "name": "Branch B"},
        {"id": 4, "name": "Sub-branch X"},
        {"id": 5, "name": "Sub-branch Y"}
    ]
    for data in stores_data:
        store = Store(data["id"], data["name"])
        hierarchy.add_store(store)
    store_map = {
        1: hierarchy.find_store(1),
        2: hierarchy.find_store(2),
        3: hierarchy.find_store(3),
        4: hierarchy.find_store(4),
        5: hierarchy.find_store(5)
    }
    if store_map[1] and store_map[2] and store_map[3] and store_map[4] and store_map[5]:
        store_map[1].children.extend([store_map[2], store_map[3]])
        store_map[2].children.append(store_map[4])
        store_map[3].children.append(store_map[5])
    print("--- Hierarchy Structure ---")
    for sid in sorted(hierarchy.stores.keys()):
        store = hierarchy.find_store(sid)
        if store:
            print(f"ID: {store.store_id}, Name: {store.name}, Parent ID: {store.parent}")
    print("\n--- Relationship Check (Descendants of HQ Store - ID 1) ---")
    hq_descendants = hierarchy.get_all_descendants(1)
    for store in hq_descendants:
        print(f"Descendant: {store.name} (ID: {store.store_id})")