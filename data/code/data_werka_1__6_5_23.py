class WeightDifferenceStore:

    def __init__(self):
        self.weights = {}

    def add_weight_pair(self, name, weight1, weight2):
        self.weights[name] = (weight1, weight2)

    def get_difference(self, name):
        if name in self.weights:
            weight1, weight2 = self.weights[name]
            return abs(weight1 - weight2)
        else:
            return None
if __name__ == '__main__':
    store = WeightDifferenceStore()
    store.add_weight_pair('pair1', 50, 30)
    store.add_weight_pair('pair2', 75, 60)
    print(store.get_difference('pair1'))
    print(store.get_difference('pair2'))