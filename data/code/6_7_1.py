class WeightStore:
    def __init__(self):
        self.weights = {}
    def add_weight_pair(self, key, weight1, weight2):
        self.weights[key] = (weight1, weight2)
    def get_difference(self, key):
        if key in self.weights:
            weight1, weight2 = self.weights[key]
            return weight1 - weight2
        return None
if __name__ == '__main__':
    store = WeightStore()
    store.add_weight_pair("A", 100, 50)
    store.add_weight_pair("B", 200, 150)
    store.add_weight_pair("C", 300, 250)
    print(f"Difference for A: {store.get_difference('A')}")
    print(f"Difference for B: {store.get_difference('B')}")
    print(f"Difference for C: {store.get_difference('C')}")
    print(f"Difference for D (non-existent): {store.get_difference('D')}")