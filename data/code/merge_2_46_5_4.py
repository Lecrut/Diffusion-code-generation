from typing import List, Set
class DifferenceSet:
    def __init__(self, collection1: List[int], collection2: List[int]):
        self.collection1 = set(collection1)
        self.collection2 = set(collection2)
    def find_difference(self) -> List[int]:
        return list(self.collection1 - self.collection2)
    def sort_results(self, results: List[int]) -> List[int]:
        return sorted(results)
    def handle_empty_inputs(self, collection1: Set[int], collection2: Set[int]) -> bool:
        if not collection1 or not collection2:
            print("Warning: One of the input collections is empty.")
            return True
        return False
if __name__ == '__main__':
    sample_collection_1 = [5, 3, 8, 9, 5]
    sample_collection_2 = [4, 7, 8, 6]
    diff_set = DifferenceSet(sample_collection_1, sample_collection_2)
    if diff_set.handle_empty_inputs(diff_set.collection1, diff_set.collection2):
        print("Proceeding with empty input handling.")
    difference_result = diff_set.find_difference()
    sorted_result = diff_set.sort_results(difference_result)
    print(f"Difference Set: {difference_result}")
    print(f"Sorted Difference Set: {sorted_result}")