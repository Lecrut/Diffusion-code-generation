class WeightDifferenceStore:
    def __init__(self):
        self.data = {}

    def add_pair(self, key, weight_a, weight_b):
        self.data[key] = {'weight_a': weight_a, 'weight_b': weight_b, 'difference': weight_a - weight_b}

    def get_difference(self, key):
        if key not in self.data:
            return None
        return self.data[key]['difference']

def main():
    store = WeightDifferenceStore()
    store.add_pair('item1', 10, 3)
    store.add_pair('item2', 20, 5)
    store.add_pair('item3', 100, 90)
    print(store.get_difference('item1'))
    print(store.get_difference('item2'))
    print(store.get_difference('item3'))
    print(store.get_difference('missing'))

if __name__ == '__main__':
    main()