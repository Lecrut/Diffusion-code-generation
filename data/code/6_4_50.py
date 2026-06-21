class WeightManager:

    def __init__(self):
        self.weight_dict = {}

    def store_weights(self, key, weight1, weight2):
        if not isinstance(key, str) or not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
            raise ValueError('Invalid input types')
        self.weight_dict[key] = (weight1, weight2)

    def calculate_difference(self, key):
        if key not in self.weight_dict:
            raise KeyError(f'No weights found for key: {key}')
        weight1, weight2 = self.weight_dict[key]
        return abs(weight1 - weight2)
if __name__ == '__main__':
    manager = WeightManager()
    manager.store_weights('apple', 150, 120)
    manager.store_weights('banana', 80, 100)
    print(manager.calculate_difference('apple'))
    print(manager.calculate_difference('banana'))