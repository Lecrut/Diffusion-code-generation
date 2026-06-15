class ListAnalyzer:
    def find_max_iterative(self, data):
        if not data:
            raise ValueError("List cannot be empty")
        max_val = data[0]
        for item in data[1:]:
            if item > max_val:
                max_val = item
        return max_val
    def find_max_sorting(self, data):
        if not data:
            raise ValueError("List cannot be empty")
        sorted_data = sorted(data)
        return sorted_data[-1]
    def find_max_max(self, data):
        if not data:
            raise ValueError("List cannot be empty")
        return max(data)
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = [15, 8, 22, 4, 30, 11]
    print(f"Sample List: {sample_list}\n")
    try:
        max_iterative = analyzer.find_max_iterative(sample_list)
        print(f"Method 1 (Iterative): Maximum element is {max_iterative}")
        max_sorting = analyzer.find_max_sorting(sample_list)
        print(f"Method 2 (Sorting): Maximum element is {max_sorting}")
        max_builtin = analyzer.find_max_max(sample_list)
        print(f"Method 3 (max()): Maximum element is {max_builtin}")
    except ValueError as e:
        print(f"Error: {e}")