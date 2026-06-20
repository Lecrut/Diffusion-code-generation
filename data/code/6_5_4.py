class WeightPairStore:
    def __init__(self):
        self.pairs = {}

    def add_pair(self, first, second):
        key = (first, second)
        self.pairs[key] = abs(first - second)

    def get_difference(self, first, second):
        key = (first, second)
        if key not in self.pairs:
            raise KeyError(f"Pair {key} not found in store")
        return self.pairs[key]

def main():
    store = WeightPairStore()
    store.add_pair(10, 3)
    store.add_pair(25, 25)
    store.add_pair(100, 1)
    diff1 = store.get_difference(10, 3)
    diff2 = store.get_difference(25, 25)
    diff3 = store.get_difference(100, 1)
    print(diff1)
    print(diff2)
    print(diff3)

if __name__ == '__main__':
    main()