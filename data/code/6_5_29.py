class WeightDifferenceStore:

    def __init__(self):
        self.weights = {}

    def store_pair(self, key, weight1, weight2):
        self.weights[key] = (weight1, weight2)

    def get_difference(self, key):
        if key in self.weights:
            weight1, weight2 = self.weights[key]
            return abs(weight1 - weight2)
        else:
            raise KeyError('Key not found')
if __name__ == '__main__':
    store = WeightDifferenceStore()
    store.store_pair('pair1', 100, 75)
    store.store_pair('pair2', 200, 150)
    print(store.get_difference('pair1'))
    print(store.get_difference('pair2'))