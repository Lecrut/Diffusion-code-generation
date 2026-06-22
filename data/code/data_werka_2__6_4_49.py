class WeightDifferenceManager:
    def __init__(self):
        self.weight_data = {}

    def store_weight_pair(self, identifier, weight1, weight2):
        self.weight_data[identifier] = (weight1, weight2)

    def calculate_difference(self, identifier):
        if identifier not in self.weight_data:
            raise ValueError(f"No data found for identifier: {identifier}")
        weight1, weight2 = self.weight_data[identifier]
        return abs(weight1 - weight2)

if __name__ == '__main__':
    manager = WeightDifferenceManager()
    manager.store_weight_pair('itemA', 80, 60)
    manager.store_weight_pair('itemB', 45, 95)
    print(manager.calculate_difference('itemA'))
    print(manager.calculate_difference('itemB'))