class WeightStore:
    def __init__(self):
        self.weight_pairs = {}

    def add_pair(self, key, weight1, weight2):
        if not isinstance(key, str) or not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
            raise ValueError('Invalid input types')
        self.weight_pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self.weight_pairs:
            raise ValueError('Key not found')
        weight1, weight2 = self.weight_pairs[key]
        return abs(weight1 - weight2)

if __name__ == '__main__':
    ws = WeightStore()
    ws.add_pair('pairA', 45.5, 30.0)
    ws.add_pair('pairB', 60.0, 90.5)
    print(ws.get_difference('pairA'))
    print(ws.get_difference('pairB'))