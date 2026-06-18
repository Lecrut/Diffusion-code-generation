class DifferenceSet:
    def __init__(self):
        self.collection_a = []
        self.collection_b = []
    def set_difference(self):
        if not self.collection_a and not self.collection_b:
            return []
        result_set = set()
        for item in self.collection_a:
            if item not in self.collection_b:
                result_set.add(item)
        return list(result_set)
    def sort_difference(self, reverse=False):
        diff_list = self.set_difference()
        sorted_diff = sorted(diff_list, reverse=reverse)
        return sorted_diff
    def handle_empty_inputs(self):
        if not self.collection_a or not self.collection_b:
            raise ValueError("At least one collection must be provided.")
if __name__ == '__main__':
    diff_set = DifferenceSet()
    diff_set.collection_a = [1, 2, 3, 4]
    diff_set.collection_b = [2, 3, 5]
    result_unsorted = diff_set.set_difference()
    print("Unsorted difference:", result_unsorted)
    result_sorted_asc = diff_set.sort_difference(reverse=False)
    print("Sorted ascending:", result_sorted_asc)
    result_sorted_desc = diff_set.sort_difference(reverse=True)
    print("Sorted descending:", result_sorted_desc)
    try:
        test_obj = DifferenceSet()
        test_obj.collection_a = []
        test_obj.handle_empty_inputs()
    except ValueError as e:
        print(f"Caught expected error for empty input: {e}")
    diff_set2 = DifferenceSet()
    diff_set2.collection_a = [1, 2]
    diff_set2.collection_b = []
    result_mixed_empty = diff_set2.set_difference()
    print("Difference where B is empty:", result_mixed_empty)