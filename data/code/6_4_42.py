class WeightStorage:
    def __init__(self):
        self.weight_pairs = {}

    def store_pair(self, key, weight1, weight2):
        self.weight_pairs[key] = (weight1, weight2)

    def calculate_difference(self, key):
        if key not in self.weight_pairs:
            raise ValueError(f'Key {key} does not exist in storage')
        weight1, weight2 = self.weight_pairs[key]
        return abs(weight1 - weight2)

if __name__ == '__main__':
    ws = WeightStorage()
    ws.store_pair('pairA', 45, 60)
    ws.store_pair('pairB', 80, 30)
    print(ws.calculate_difference('pairA'))
    print(ws.calculate_difference('pairB'))