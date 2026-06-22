class WeightPairManager:
    def __init__(self):
        self.pairs = {}

    def add_pair(self, key, weight1, weight2):
        self.pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self.pairs:
            raise KeyError(key)
        weight1, weight2 = self.pairs[key]
        return abs(weight1 - weight2)

if __name__ == '__main__':
    manager = WeightPairManager()
    manager.add_pair('pair1', 10, 20)
    manager.add_pair('pair2', 5, 15)
    manager.add_pair('pair3', 30, 10)
    print(manager.get_difference('pair1'))
    print(manager.get_difference('pair2'))
    print(manager.get_difference('pair3'))