class WeightDifference:

    def __init__(self):
        self.weights = {}

    def add_pair(self, name, weight1, weight2):
        self.weights[name] = (weight1, weight2)

    def get_difference(self, name):
        if name not in self.weights:
            raise ValueError(f'No pair with the name {name} found.')
        weight1, weight2 = self.weights[name]
        return abs(weight1 - weight2)
if __name__ == '__main__':
    wd = WeightDifference()
    wd.add_pair('pair1', 50, 30)
    wd.add_pair('pair2', 70, 90)
    print(wd.get_difference('pair1'))
    print(wd.get_difference('pair2'))