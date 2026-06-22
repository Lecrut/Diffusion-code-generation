class WeightPairStore:
    def __init__(self):
        self.pairs = {}

    def add_pair(self, name, weight1, weight2):
        self.pairs[name] = (weight1, weight2)

    def get_difference(self, name):
        if name not in self.pairs:
            raise KeyError(f"Pair '{name}' not found")
        w1, w2 = self.pairs[name]
        return abs(w1 - w2)

    def retrieve_pair(self, name):
        if name not in self.pairs:
            raise KeyError(f"Pair '{name}' not found")
        return self.pairs[name]

if __name__ == '__main__':
    store = WeightPairStore()
    store.add_pair("item_A", 150, 120)
    store.add_pair("item_B", 300, 315)
    store.add_pair("item_C", 50, 50)
    
    diff_a = store.get_difference("item_A")
    diff_b = store.get_difference("item_B")
    pair_c = store.retrieve_pair("item_C")
    
    print(diff_a)
    print(diff_b)
    print(pair_c)