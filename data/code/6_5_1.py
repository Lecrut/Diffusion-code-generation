class WeightPairStore:
    def __init__(self):
        self._pairs = {}

    def add_pair(self, name, weight_a, weight_b):
        self._pairs[name] = (weight_a, weight_b)

    def get_difference(self, name):
        if name not in self._pairs:
            raise KeyError(f"Pair '{name}' not found")
        weight_a, weight_b = self._pairs[name]
        return weight_a - weight_b

    def retrieve_pair(self, name):
        if name not in self._pairs:
            raise KeyError(f"Pair '{name}' not found")
        return self._pairs[name]

if __name__ == '__main__':
    store = WeightPairStore()
    store.add_pair("item_a", 100, 85)
    store.add_pair("item_b", 200, 150)
    store.add_pair("item_c", 30, 45)
    diff_a = store.get_difference("item_a")
    diff_b = store.get_difference("item_b")
    diff_c = store.get_difference("item_c")
    print(diff_a)
    print(diff_b)
    print(diff_c)