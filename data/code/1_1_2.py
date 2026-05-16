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
    manager = WeightManager()
    manager.store_weight("Alice", 65.5)
    manager.store_weight("Bob", 82.1)
    manager.store_weight("Charlie", 70.0)
    print("Alice's initial weight:", manager.get_weight("Alice"))
    print("Bob's initial weight:", manager.get_weight("Bob"))
    manager.update_weight("Alice", 66.0)
    print("Alice's updated weight:", manager.get_weight("Alice"))
    manager.update_weight("David", 95.5)
    print("David's weight:", manager.get_weight("David"))
    print("Charlie's weight:", manager.get_weight("Charlie"))
    print("Non-existent weight:", manager.get_weight("Eve"))