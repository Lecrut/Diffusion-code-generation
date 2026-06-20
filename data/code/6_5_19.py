class WeightPairStorage:
    def __init__(self):
        self._pairs = {}

    def add_pair(self, key, weight1, weight2):
        self._pairs[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self._pairs:
            return None
        w1, w2 = self._pairs[key]
        return w1 - w2

    def get_all_differences(self):
        return {k: w1 - w2 for k, (w1, w2) in self._pairs.items()}

if __name__ == '__main__':
    storage = WeightPairStorage()
    storage.add_pair('apple', 150.5, 145.2)
    storage.add_pair('banana', 120.0, 115.5)
    storage.add_pair('cherry', 80.3, 80.3)

    diff_apple = storage.get_difference('apple')
    print(f"Difference for 'apple': {diff_apple}")

    diff_banana = storage.get_difference('banana')
    print(f"Difference for 'banana': {diff_banana}")

    diff_cherry = storage.get_difference('cherry')
    print(f"Difference for 'cherry': {diff_cherry}")

    all_diffs = storage.get_all_differences()
    print(f"All differences: {all_diffs}")