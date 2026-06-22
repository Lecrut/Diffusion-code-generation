class WeightPairStore:
    def __init__(self):
        self.pairs = {}

    def add_pair(self, label, weight_a, weight_b):
        self.pairs[label] = (weight_a, weight_b)

    def get_difference(self, label):
        if label not in self.pairs:
            raise KeyError(f"Label '{label}' not found in store")
        weight_a, weight_b = self.pairs[label]
        return weight_a - weight_b

if __name__ == '__main__':
    store = WeightPairStore()
    store.add_pair('item_1', 150, 120)
    store.add_pair('item_2', 80, 95)
    store.add_pair('item_3', 200, 200)
    diff_1 = store.get_difference('item_1')
    diff_2 = store.get_difference('item_2')
    diff_3 = store.get_difference('item_3')
    print(diff_1)
    print(diff_2)
    print(diff_3)