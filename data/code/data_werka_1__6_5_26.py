class WeightManager:

    def __init__(self):
        self.weights = {}

    def add_pair(self, key, weight1, weight2):
        self.weights[key] = (weight1, weight2)

    def get_difference(self, key):
        if key in self.weights:
            weight1, weight2 = self.weights[key]
            return abs(weight1 - weight2)
        else:
            return None
if __name__ == '__main__':
    manager = WeightManager()
    manager.add_pair('pair1', 50, 70)
    manager.add_pair('pair2', 30, 40)
    manager.add_pair('pair3', 80, 60)
    print(manager.get_difference('pair1'))
    print(manager.get_difference('pair2'))
    print(manager.get_difference('pair3'))