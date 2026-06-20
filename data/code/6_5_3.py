class WeightDifferenceStore:
    def __init__(self):
        self._storage = {}

    def store_pair(self, label, weight_a, weight_b):
        self._storage[label] = (weight_a, weight_b)

    def get_difference(self, label):
        if label not in self._storage:
            raise KeyError(f"No pair found with label: {label}")
        weight_a, weight_b = self._storage[label]
        return weight_a - weight_b

    def has_pair(self, label):
        return label in self._storage

if __name__ == '__main__':
    store = WeightDifferenceStore()
    store.store_pair("sample_one", 150, 120)
    store.store_pair("sample_two", 200, 250)
    diff_one = store.get_difference("sample_one")
    diff_two = store.get_difference("sample_two")
    print(diff_one)
    print(diff_two)