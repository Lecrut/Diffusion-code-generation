class DifferenceSet:
    def __init__(self, collection_a, collection_b):
        self.collection_a = set(collection_a) if not isinstance(collection_a, (set, frozenset)) else collection_a
        self.collection_b = set(collection_b) if not isinstance(collection_b, (set, frozenset)) else collection_b
    def get_difference(self):
        return list(self.collection_a - self.collection_b)
    def sort_results(self, key=None, reverse=False):
        results = sorted(self.get_difference(), key=key, reverse=reverse)
        return results
    def is_empty_input_handling(self):
        if not self.collection_a or not self.collection_b:
            raise ValueError("At least one collection must be provided.")
if __name__ == '__main__':
    sample_list_1 = [3, 5, 7, 9]
    sample_list_2 = [4, 6, 8, 10]
    diff_set = DifferenceSet(sample_list_1, sample_list_2)
    print("Difference set:", diff_set.get_difference())
    sorted_diff = diff_set.sort_results(reverse=True)
    print("Sorted difference (descending):", sorted_diff)