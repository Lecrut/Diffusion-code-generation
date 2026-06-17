class DifferenceSet:
    def __init__(self):
        self.collection_a = []
        self.collection_b = []
    def set_difference(self, a=None, b=None):
        if a is None and len(self.collection_a) == 0:
            raise ValueError("Collection A must be provided or initialized.")
        if b is None and len(self.collection_b) == 0:
            raise ValueError("Collection B must be provided or initialized.")
        self.collection_a = list(a) if a else []
        self.collection_b = list(b) if b else []
        result_set = set()
        for item in self.collection_a:
            if item not in self.collection_b:
                result_set.add(item)
        return sorted(list(result_set))
    def sort_results(self, results):
        try:
            return sorted(results)
        except TypeError:
            raise ValueError("Items must be sortable.")
if __name__ == '__main__':
    diff = DifferenceSet()
    sample_a = [3, 1, 4, 5]
    sample_b = [2, 3, 6]
    result = diff.set_difference(sample_a, sample_b)
    print(f"Difference Set: {result}")
    test_list = [5, 2, 8]
    sorted_test = diff.sort_results(test_list)
    print(f"Sorted List: {sorted_test}")