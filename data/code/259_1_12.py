class MinMaxFinder:
    @staticmethod
    def find_min_max(data):
        if not data:
            raise ValueError("Data list cannot be empty")
        min_val = float('inf')
        max_val = float('-inf')
        for num in data:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        return min_val, max_val

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    finder = MinMaxFinder()
    result = finder.find_min_max(sample_list)
    print(result)