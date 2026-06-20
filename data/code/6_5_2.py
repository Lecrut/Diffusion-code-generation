class WeightPairStore:
    def __init__(self):
        self._pairs = {}

    def add_pair(self, weight1, weight2):
        key = (weight1, weight2)
        self._pairs[key] = abs(weight1 - weight2)

    def get_difference(self, weight1, weight2):
        key = (weight1, weight2)
        if key in self._pairs:
            return self._pairs[key]
        return None

if __name__ == '__main__':
    store = WeightPairStore()
    store.add_pair(10, 25)
    store.add_pair(100, 50)
    result = store.get_difference(10, 25)
    print(result)
    result2 = store.get_difference(100, 50)
    print(result2)
    result3 = store.get_difference(10, 100)
    print(result3)