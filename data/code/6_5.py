class WeightPairStore:
    def __init__(self):
        self._data = {}

    def add_pair(self, key, weight1, weight2):
        self._data[key] = (weight1, weight2)

    def get_difference(self, key):
        if key not in self._data:
            raise KeyError(f"Key '{key}' not found.")
        w1, w2 = self._data[key]
        return w1 - w2

if __name__ == '__main__':
    store = WeightPairStore()
    store.add_pair("pair1", 100, 50)
    store.add_pair("pair2", 3.5, 2.5)
    
    diff1 = store.get_difference("pair1")
    diff2 = store.get_difference("pair2")
    
    print(diff1)
    print(diff2)