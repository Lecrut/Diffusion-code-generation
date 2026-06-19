class WeightDifference:

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
    wd = WeightDifference()
    wd.store_pair('pair1', 50, 30)
    wd.store_pair('pair2', 70, 90)
    print(wd.get_difference('pair1'))
    print(wd.get_difference('pair2'))