class WeightManager:
    def __init__(self):
        self.weight_dict = {}

    def store_pair(self, identifier, first_weight, second_weight):
        self.weight_dict[identifier] = (first_weight, second_weight)

    def calculate_difference(self, identifier):
        if identifier not in self.weight_dict:
            raise ValueError('Identifier not found')
        weight_one, weight_two = self.weight_dict[identifier]
        return abs(weight_one - weight_two)

if __name__ == '__main__':
    manager = WeightManager()
    manager.store_pair('itemA', 25, 40)
    manager.store_pair('itemB', 60, 30)
    difference_A = manager.calculate_difference('itemA')
    difference_B = manager.calculate_difference('itemB')
    print(difference_A)
    print(difference_B)