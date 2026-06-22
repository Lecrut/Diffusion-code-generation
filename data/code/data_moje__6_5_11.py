class WeightPairStore:
    def __init__(self):
        self._pairs = {}

    def add_pair(self, key, weight1, weight2):
        self._pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self._pairs:
            raise KeyError(f"Key '{key}' not found in storage.")
        weight1, weight2 = self._pairs[key]
        return weight1 - weight2

    def get_all_differences(self):
        return {
            k: w1 - w2 for k, (w1, w2) in self._pairs.items()
        }

if __name__ == '__main__':
    store = WeightPairStore()
    store.add_pair('apple', 150.5, 100.0)
    store.add_pair('banana', 80.0, 75.5)
    store.add_pair('orange', 200.0, 120.0)

    diff_apple = store.get_difference('apple')
    all_diffs = store.get_all_differences()

    print(diff_apple)
    print(all_diffs)