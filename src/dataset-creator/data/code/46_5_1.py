class DifferenceSet:
    def __init__(self):
        self.collection_a = []
        self.collection_b = []
    def set_difference(self):
        if not self.collection_a and not self.collection_b:
            return []
        result = [item for item in self.collection_a if item not in self.collection_b]
        return result
    def sort_results(self, results=None):
        if results is None:
            results = self.set_difference()
        try:
            sorted_results = sorted(results)
        except TypeError:
            print("Error: Collection items must be comparable.")
            raise
        return sorted_results
if __name__ == '__main__':
    diff_set = DifferenceSet()
    diff_set.collection_a = [3, 1, 4, 5]
    diff_set.collection_b = [2, 4]
    result_diff = diff_set.set_difference()
    print("Difference set:", result_diff)
    sorted_result = diff_set.sort_results(result_diff)
    print("Sorted difference set:", sorted_result)