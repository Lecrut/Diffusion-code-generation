import itertools

class ListAnalyzer:
    def __init__(self, *lists):
        self.lists = lists
        self.combined = list(itertools.chain.from_iterable(lists))

    def find_global_min_max(self):
        global_min = min(self.combined)
        global_max = max(self.combined)
        min_list_name = next((f"list{i+1}" for i, lst in enumerate(self.lists) if global_min in lst), None)
        max_list_name = next((f"list{i+1}" for i, lst in enumerate(self.lists) if global_max in lst), None)
        return (global_min, min_list_name), (global_max, max_list_name)

if __name__ == '__main__':
    analyzer = ListAnalyzer([3, 5, 1, 8], [4, 9, 2, 7], [6, 0, 3, 5])
    min_result, max_result = analyzer.find_global_min_max()
    print(f"Global Min: {min_result[0]} from {min_result[1]}")
    print(f"Global Max: {max_result[0]} from {max_result[1]}")