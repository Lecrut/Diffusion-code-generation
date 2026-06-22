class WeightPairStorage:
    def __init__(self):
        self._store = {}

    def add_pair(self, label, w1, w2):
        self._store[label] = (w1, w2)

    def get_difference(self, label):
        if label not in self._store:
            raise KeyError(label)
        w1, w2 = self._store[label]
        return w1 - w2

if __name__ == '__main__':
    storage = WeightPairStorage()
    storage.add_pair("apple_box", 10.5, 2.3)
    storage.add_pair("metal_plate", 50.0, 12.5)
    
    diff = storage.get_difference("apple_box")
    print(diff)
    
    diff_metal = storage.get_difference("metal_plate")
    print(diff_metal)