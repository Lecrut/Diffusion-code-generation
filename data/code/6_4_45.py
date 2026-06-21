class WeightStore:
    def __init__(self):
        self.weight_data = {}

    def store_pair(self, key, weight1, weight2):
        self.weight_data[key] = (weight1, weight2)

    def calculate_difference(self, key):
        if key not in self.weight_data:
            raise ValueError('Key not found')
        weight1, weight2 = self.weight_data[key]
        return abs(weight1 - weight2)

if __name__ == '__main__':
    weight_store = WeightStore()
    weight_store.store_pair('example1', 45, 60)
    weight_store.store_pair('example2', 80, 35)
    print(weight_store.calculate_difference('example1'))
    print(weight_store.calculate_difference('example2'))