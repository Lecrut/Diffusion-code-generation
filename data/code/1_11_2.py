class WeightManager:
    def __init__(self):
        self.weights = {}
    def store_weight(self, name, weight):
        self.weights[name] = weight
    def get_weight(self, name):
        return self.weights.get(name)
    def update_weight(self, name, new_weight):
        if name in self.weights:
            self.weights[name] = new_weight
        else:
            self.store_weight(name, new_weight)
if __name__ == '__main__':
    wm = WeightManager()
    wm.store_weight("Alice", 65.5)
    wm.store_weight("Bob", 82.1)
    wm.store_weight("Charlie", 70.0)
    print("Alice's weight:", wm.get_weight("Alice"))
    print("Bob's weight:", wm.get_weight("Bob"))
    print("David's weight (non-existent):", wm.get_weight("David"))
    wm.update_weight("Alice", 68.0)
    print("Alice's updated weight:", wm.get_weight("Alice"))
    wm.update_weight("Eve", 55.2)
    print("Eve's weight:", wm.get_weight("Eve"))