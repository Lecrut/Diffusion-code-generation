class WeightPairManager:
    def __init__(self):
        self.pairs = {}

    def store_pair(self, name, weight_a, weight_b):
        self.pairs[name] = (weight_a, weight_b)

    def get_difference(self, name):
        if name not in self.pairs:
            raise KeyError(f"Pair '{name}' not found")
        weight_a, weight_b = self.pairs[name]
        return weight_a - weight_b

    def remove_pair(self, name):
        if name in self.pairs:
            del self.pairs[name]

if __name__ == '__main__':
    manager = WeightPairManager()
    manager.store_pair("fruit_apple", 150, 120)
    manager.store_pair("fruit_banana", 80, 90)
    manager.store_pair("package_box", 2000, 1800)
    
    diff_apple = manager.get_difference("fruit_apple")
    diff_banana = manager.get_difference("fruit_banana")
    diff_box = manager.get_difference("package_box")
    
    print(diff_apple)
    print(diff_banana)
    print(diff_box)