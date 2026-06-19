class WeightDifferenceStore:

    def __init__(self):
        self.weight_pairs = {}

    def add_pair(self, key, weight1, weight2):
        self.weight_pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key in self.weight_pairs:
            weight1, weight2 = self.weight_pairs[key]
            return abs(weight1 - weight2)
        else:
            raise KeyError('Key not found')
if __name__ == '__main__':
    store = WeightDifferenceStore()
    store.add_pair('pair1', 50, 30)
    store.add_pair('pair2', 70, 90)
    print(store.get_difference('pair1'))
    print(store.get_difference('pair2'))