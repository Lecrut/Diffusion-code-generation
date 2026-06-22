class WeightPairStore:
    def __init__(self):
        self.pairs = {}

    def add_pair(self, key, weight1, weight2):
        self.pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self.pairs:
            raise KeyError(f"Key {key} not found")
        w1, w2 = self.pairs[key]
        return w1 - w2

if __name__ == '__main__':
    store = WeightPairStore()
    store.add_pair('pair1', 10, 4)
    store.add_pair('pair2', 20, 7)
    store.add_pair('pair3', 100, 50)

    print(store.get_difference('pair1'))
    print(store.get_difference('pair2'))
    print(store.get_difference('pair3'))