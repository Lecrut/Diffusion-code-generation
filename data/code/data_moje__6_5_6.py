class WeightPairStore:
    def __init__(self):
        self.pairs = {}

    def add_pair(self, key, weight1, weight2):
        self.pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self.pairs:
            raise KeyError(f"Key {key} not found in weight pairs.")
        weight1, weight2 = self.pairs[key]
        return weight1 - weight2

if __name__ == '__main__':
    store = WeightPairStore()
    store.add_pair('pair1', 10.5, 8.2)
    store.add_pair('pair2', 5.0, 3.5)
    store.add_pair('pair3', 100, 75)
    diff1 = store.get_difference('pair1')
    diff2 = store.get_difference('pair2')
    diff3 = store.get_difference('pair3')
    print(diff1)
    print(diff2)
    print(diff3)