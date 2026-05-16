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
            self.weights[name] = new_weight
if __name__ == '__main__':
    wm = WeightManager()
    wm.store_weight("Alice", 65.5)
    wm.store_weight("Bob", 82.1)
    wm.store_weight("Charlie", 70.0)
    print("Alice's initial weight:", wm.get_weight("Alice"))
    print("Bob's initial weight:", wm.get_weight("Bob"))
    wm.update_weight("Alice", 66.0)
    print("Alice's updated weight:", wm.get_weight("Alice"))
    wm.update_weight("David", 90.5)
    print("David's weight:", wm.get_weight("David"))
    print("Charlie's weight:", wm.get_weight("Charlie"))
    print("Non-existent weight:", wm.get_weight("Eve"))