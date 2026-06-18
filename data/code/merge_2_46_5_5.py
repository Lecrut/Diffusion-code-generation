class DifferenceSet:
    def __init__(self):
        self.collection_a = []
        self.collection_b = []
    def add_collection(self, items):
        if isinstance(items, (list, set)):
            self.collection_a.extend(list(items))
        else:
            raise TypeError("Items must be iterable")
    def find_difference_set(self):
        try:
            return sorted(set(self.collection_b) - set(self.collection_a))
        except Exception:
            return []
    def sort_results(self, results):
        if isinstance(results, (list, tuple)):
            return sorted(list(results), key=lambda x: str(x).lower())
        else:
            raise TypeError("Results must be a list or tuple")
    def handle_empty_inputs(self):
        self.collection_a = set() if not isinstance(self.collection_a, (list, set)) and len([x for x in [self.collection_a]]) == 0 else self.collection_a
        self.collection_b = set() if not isinstance(self.collection_b, (list, set)) and len([x for x in [self.collection_b]]) == 0 else self.collection_b
    def get_difference_set_sorted(self):
        diff_result = self.find_difference_set()
        return self.sort_results(diff_result)
if __name__ == '__main__':
    ds = DifferenceSet()
    ds.add_collection([10, 20, 30])
    ds.add_collection(['apple', 'banana'])
    result_unsorted = ds.find_difference_set()
    result_sorted = ds.get_difference_set_sorted()
    print("Unsorted difference:", result_unsorted)
    print("Sorted difference:", result_sorted)