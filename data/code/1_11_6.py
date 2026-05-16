class WeightManager:
    def __init__(self):
        self.weights = {}
    def store_weight(self, name, weight):
        self.weights[name] = weight
    def retrieve_weight(self, name):
        return self.weights.get(name)
    def update_weight(self, name, new_weight):
        if name in self.weights:
            self.weights[name] = new_weight
        else:
            self.weights[name] = new_weight
if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weight("Alice", 65.5)
    manager.store_weight("Bob", 82.1)
    manager.store_weight("Charlie", 70.0)
    print("Initial weights:")
    print("Alice:", manager.retrieve_weight("Alice"))
    print("Bob:", manager.retrieve_weight("Bob"))
    print("Charlie:", manager.retrieve_weight("Charlie"))
    manager.update_weight("Alice", 66.0)
    print("\nUpdated weights:")
    print("Alice:", manager.retrieve_weight("Alice"))
    print("Bob:", manager.retrieve_weight("Bob"))
    print("Charlie:", manager.retrieve_weight("Charlie"))
    manager.update_weight("David", 95.5)
    print("\nWeights after adding David:")
    print("David:", manager.retrieve_weight("David"))
    print("Alice:", manager.retrieve_weight("Alice"))