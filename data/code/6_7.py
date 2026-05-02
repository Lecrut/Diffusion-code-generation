class WeightStore:
    def __init__(self):
        self.weight_pairs = {}
    def add_pair(self, key, weight1, weight2):
        self.weight_pairs[key] = (weight1, weight2)
    def get_difference(self, key):
        if key in self.weight_pairs:
            weight1, weight2 = self.weight_pairs[key]
            return weight1 - weight2
        return None
if __name__ == '__main__':
    store = WeightStore()
    store.add_pair("A", 100, 50)
    store.add_pair("B", 200, 150)
    store.add_pair("C", 300, 100)
    print(f"Difference for A: {store.get_difference('A')}")
    print(f"Difference for B: {store.get_difference('B')}")
    print(f"Difference for C: {store.get_difference('C')}")
    print(f"Difference for D (non-existent): {store.get_difference('D')}")