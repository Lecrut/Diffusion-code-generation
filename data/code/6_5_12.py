class WeightPairManager:
    def __init__(self):
        self.pairs = {}

    def add_pair(self, key, weight1, weight2):
        self.pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self.pairs:
            raise KeyError(f"Key '{key}' not found in weight pairs.")
        w1, w2 = self.pairs[key]
        return abs(w1 - w2)

if __name__ == '__main__':
    manager = WeightPairManager()
    manager.add_pair("apple", 150, 200)
    manager.add_pair("banana", 100, 130)
    manager.add_pair("orange", 300, 280)

    diff_apple = manager.get_difference("apple")
    diff_banana = manager.get_difference("banana")
    diff_orange = manager.get_difference("orange")

    print(diff_apple)
    print(diff_banana)
    print(diff_orange)