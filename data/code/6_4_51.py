class WeightDifferenceManager:
    def __init__(self):
        self.weight_data = {}

    def store_weights(self, key, weight1, weight2):
        self.weight_data[key] = (weight1, weight2)

    def calculate_difference(self, key):
        if key not in self.weight_data:
            raise ValueError('Key not found')
        weight1, weight2 = self.weight_data[key]
        return abs(weight1 - weight2)

if __name__ == '__main__':
    manager = WeightDifferenceManager()
    manager.store_weights('pairA', 80, 60)
    manager.store_weights('pairB', 45, 95)
    print(manager.calculate_difference('pairA'))
    print(manager.calculate_difference('pairB'))