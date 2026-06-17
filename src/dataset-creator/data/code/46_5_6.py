class DifferenceSet:
    def __init__(self, collection_a, collection_b):
        self.collection_a = set(collection_a) if not isinstance(collection_a, (set, frozenset)) else collection_a
        self.collection_b = set(collection_b) if not isinstance(collection_b, (set, frozenset)) else collection_b
    def get_difference(self):
        return list(self.collection_a - self.collection_b)
    def sort_result(self, reverse=False):
        sorted_diff = sorted(self.get_difference(), reverse=reverse)
        return DifferenceSet(sorted_diff, [])
    @staticmethod
    def handle_empty_inputs(collection_a, collection_b):
        if not collection_a and not collection_b:
            raise ValueError("Both collections are empty.")
        elif not collection_a or not collection_b:
            print(f"Warning: One of the input collections is empty. A={collection_a}, B={collection_b}")
    def __str__(self):
        return f"DifferenceSet({list(self.collection_a - self.collection_b)})"
if __name__ == '__main__':
    sample_set_1 = [3, 5, 7, 9]
    sample_set_2 = [4, 6, 8, 10]
    diff_calc = DifferenceSet(sample_set_1, sample_set_2)
    try:
        result = diff_calc.get_difference()
        print(f"Difference Set: {result}")
        sorted_result = diff_calc.sort_result(reverse=True)
        print(f"Sorted Result (Descending): {sorted_result.collection_a - set()}")
        empty_diff = DifferenceSet([], [1, 2])
        result_empty = empty_diff.get_difference()
        print(f"Difference with one empty input: {result_empty}")
    except ValueError as e:
        print(f"Error occurred: {e}")