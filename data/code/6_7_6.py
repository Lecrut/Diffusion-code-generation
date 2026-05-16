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
    store.add_weight_pair("pair1", 10, 4)
    store.add_weight_pair("pair2", 25, 15)
    store.add_weight_pair("pair3", 50, 20)
    print(f"Difference for pair1: {store.get_difference('pair1')}")
    print(f"Difference for pair2: {store.get_difference('pair2')}")
    print(f"Difference for pair3: {store.get_difference('pair3')}")
    print(f"Difference for non-existent pair: {store.get_difference('pair4')}")