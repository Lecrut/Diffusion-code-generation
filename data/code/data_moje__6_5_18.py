class WeightPairStore:
    def __init__(self):
        self.pairs = {}

    def add_pair(self, first_weight, second_weight):
        self.pairs[first_weight] = second_weight

    def get_difference(self, first_weight):
        if first_weight not in self.pairs:
            raise KeyError("Weight pair not found")
        return abs(first_weight - self.pairs[first_weight])

if __name__ == '__main__':
    store = WeightPairStore()
    store.add_pair(100, 150)
    store.add_pair(80, 120)
    store.add_pair(200, 210)
    print(store.get_difference(100))
    print(store.get_difference(80))
    print(store.get_difference(200))