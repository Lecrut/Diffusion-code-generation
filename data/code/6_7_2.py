class WeightPairStore:
    def __init__(self):
        self.weight_pairs = {}
    def add_pair(self, weight1, weight2):
        key = (weight1, weight2)
        self.weight_pairs[key] = weight1 - weight2
    def get_difference(self, weight1, weight2):
        key = (weight1, weight2)
        if key in self.weight_pairs:
            return self.weight_pairs[key]
        return None
if __name__ == '__main__':
    store = WeightPairStore()
    store.add_pair(10, 5)
    store.add_pair(20, 8)
    store.add_pair(15, 10)
    print(f"Difference for (10, 5): {store.get_difference(10, 5)}")
    print(f"Difference for (20, 8): {store.get_difference(20, 8)}")
    print(f"Difference for (15, 10): {store.get_difference(15, 10)}")
    print(f"Difference for (10, 10): {store.get_difference(10, 10)}")
    print(f"Difference for (5, 10): {store.get_difference(5, 10)}")