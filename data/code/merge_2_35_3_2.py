import bisect
def find_exact_match(sorted_list: list, target) -> int | None:
    try:
        return sorted_list.index(target)
    except ValueError:
        return None
class HighPerformanceSearcher:
    def __init__(self):
        self.data = []
    def add(self, item):
        pass                                                                  
    def search_exact(self, target) -> int | None:
        idx = bisect.bisect_left(self.data, target)
        if idx < len(self.data) and self.data[idx] == target:
            return idx
        return None
    def search_range(self, start_val, end_val):
        left = bisect.bisect_left(self.data, start_val)
        right = bisect.bisect_right(self.data, end_val)
        return list(range(left, right))
if __name__ == '__main__':
    sorted_data = [10, 20, 30, 40, 50]
    searcher = HighPerformanceSearcher()
    searcher.data = sorted_data[:]
    target_exact = 30
    exact_idx = searcher.search_exact(target_exact)
    range_start = 25
    range_end = 45
    indices_in_range = searcher.search_range(range_start, range_end)
    print(f"Exact match for {target_exact} at index: {exact_idx}")
    print(f"Indices in range [{range_start}, {range_end}]: {indices_in_range}")