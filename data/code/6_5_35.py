class WeightDifferenceStore:

    def __init__(self):
        self.weight_pairs = {}

    def store_pair(self, key, weight1, weight2):
        self.weight_pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key in self.weight_pairs:
            weight1, weight2 = self.weight_pairs[key]
            return abs(weight1 - weight2)
        return None
if __name__ == '__main__':
    store = WeightDifferenceStore()
    store.store_pair('pair1', 70, 65)
    store.store_pair('pair2', 80, 85)
    print(store.get_difference('pair1'))
    print(store.get_difference('pair2'))