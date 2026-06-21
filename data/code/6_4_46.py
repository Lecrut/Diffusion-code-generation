class WeightPairStore:
    def __init__(self):
        self.pairs = {}
    
    def store_pair(self, key, weight1, weight2):
        self.pairs[key] = (weight1, weight2)
    
    def get_difference(self, key):
        if key not in self.pairs:
            raise ValueError('Key not found')
        weight1, weight2 = self.pairs[key]
        return abs(weight1 - weight2)

if __name__ == '__main__':
    store = WeightPairStore()
    store.store_pair('pair1', 40, 60)
    store.store_pair('pair2', 80, 20)
    print(store.get_difference('pair1'))
    print(store.get_difference('pair2'))