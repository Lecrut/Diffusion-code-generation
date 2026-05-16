class WeightManager:
    def __init__(self):
        self._weights = {}
    def store_weight(self, name, weight):
        self._weights[name] = weight
    def retrieve_weight(self, name):
        return self._weights.get(name)
    def update_weight(self, name, new_weight):
        if name in self._weights:
            self._weights[name] = new_weight
            return True
        return False
if __name__ == '__main__':
    wm = WeightManager()
    wm.store_weight("Alice", 65.5)
    wm.store_weight("Bob", 82.1)
    wm.store_weight("Charlie", 70.0)
    print("Alice's weight:", wm.retrieve_weight("Alice"))
    print("Bob's weight:", wm.retrieve_weight("Bob"))
    print("David's weight (non-existent):", wm.retrieve_weight("David"))
    updated = wm.update_weight("Alice", 68.0)
    print("Update successful:", updated)
    print("Alice's new weight:", wm.retrieve_weight("Alice"))
    not_found = wm.update_weight("Eve", 90.0)
    print("Update non-existent key successful:", not_found)
    print("Eve's weight:", wm.retrieve_weight("Eve"))