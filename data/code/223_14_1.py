class ListMaxFinder:
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
    def find_max_builtin(self, data):
        if not data:
            raise ValueError("List cannot be empty")
        return max(data)
if __name__ == '__main__':
    finder = ListMaxFinder()
    sample_list = [15, 3, 88, 42, 9, 71]
    print(f"Sample List: {sample_list}\n")
    try:
        max_iterative = finder.find_max_iterative(sample_list)
        print(f"Method (Iterative): Maximum element found is {max_iterative}")
        max_sorting = finder.find_max_sorting(sample_list)
        print(f"Method (Sorting): Maximum element found is {max_sorting}")
        max_builtin = finder.find_max_builtin(sample_list)
        print(f"Method (max()): Maximum element found is {max_builtin}")
    except ValueError as e:
        print(f"Error: {e}")