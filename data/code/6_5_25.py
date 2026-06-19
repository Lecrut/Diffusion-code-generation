class WeightDifferenceStore:

    def __init__(self):
        self.weights = {}

    def add_pair(self, key, weight1, weight2):
        self.weights[key] = (weight1, weight2)

    def get_difference(self, key):
        if key in self.weights:
            weight1, weight2 = self.weights[key]
            return abs(weight1 - weight2)
        return None
if __name__ == '__main__':
    store = WeightDifferenceStore()
    store.add_pair('pair1', 50, 30)
    store.add_pair('pair2', 75, 100)
    store.add_pair('pair3', 45, 45)
    print(store.get_difference('pair1'))
    print(store.get_difference('pair2'))
    print(store.get_difference('pair3'))