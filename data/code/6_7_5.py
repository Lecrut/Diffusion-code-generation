import math
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
        else:
            return None
if __name__ == '__main__':
    store = WeightPairStore()
    store.add_pair(10, 5)
    store.add_pair(20, 15)
    store.add_pair(30, 10)
    print(f"Difference for (10, 5): {store.get_difference(10, 5)}")
    print(f"Difference for (20, 15): {store.get_difference(20, 15)}")
    print(f"Difference for (30, 10): {store.get_difference(30, 10)}")
    print(f"Difference for (10, 20): {store.get_difference(10, 20)}")
    print(f"Difference for (50, 5): {store.get_difference(50, 5)}")