import bisect
def find_exact_match(sorted_list: list, target) -> bool:
    index = bisect.bisect_left(sorted_list, target)
    if index < len(sorted_list) and sorted_list[index] == target:
        return True
    return False
class SearchUtility:
    def __init__(self, data):
        self.data = list(data)
    def find_exact(self, value):
        idx = bisect.bisect_left(self.data, value)
        if idx < len(self.data) and self.data[idx] == value:
            return True
        return False
    def search_range(self, start_val, end_val):
        left_idx = bisect.bisect_left(self.data, start_val)
        right_idx = bisect.bisect_right(self.data, end_val)
        if left_idx >= len(self.data):
            return []
        range_data = self.data[left_idx:right_idx]
        return range_data
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    utility = SearchUtility(sample_data)
    print("Exact match for 50:", find_exact_match(sample_data, 50))
    print("Range [30, 70]:", utility.search_range(30, 70))