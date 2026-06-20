class WeightPairManager:
    def __init__(self):
        self.pairs = {}

    def add_pair(self, first_weight, second_weight):
        key = tuple(sorted([first_weight, second_weight]))
        self.pairs[key] = abs(first_weight - second_weight)

    def get_difference(self, weight_a, weight_b):
        key = tuple(sorted([weight_a, weight_b]))
        return self.pairs.get(key)

if __name__ == '__main__':
    manager = WeightPairManager()
    manager.add_pair(10, 5)
    manager.add_pair(20, 15)
    manager.add_pair(100, 90)
    print(manager.get_difference(5, 10))
    print(manager.get_difference(15, 20))
    print(manager.get_difference(90, 100))
    print(manager.get_difference(5, 20))