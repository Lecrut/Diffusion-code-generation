class WeightDifferenceStore:
    DEFAULT_KEY = 'default_pair'

    def __init__(self):
        self.weight_pairs = {}

    @staticmethod
    def calculate_difference(weight1, weight2):
        return abs(weight1 - weight2)

    def add_weight_pair(self, key, weight1, weight2):
        self.weight_pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self.weight_pairs:
            raise ValueError('Key not found')
        weight1, weight2 = self.weight_pairs[key]
        return self.calculate_difference(weight1, weight2)

if __name__ == '__main__':
    store = WeightDifferenceStore()
    store.add_weight_pair('pair1', 50, 30)
    store.add_weight_pair('pair2', 70, 90)
    print(store.get_difference('pair1'))
    print(store.get_difference('pair2'))