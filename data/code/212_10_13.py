class MinMaxFinder:
    @staticmethod
    def find_min(data):
        if not data:
            raise ValueError("Data list cannot be empty")
        min_val = data[0]
        for num in data[1:]:
            if num < min_val:
                min_val = num
        return min_val

    @staticmethod
    def find_max(data):
        if not data:
            raise ValueError("Data list cannot be empty")
        max_val = data[0]
        for num in data[1:]:
            if num > max_val:
                max_val = num
        return max_val

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8, 7, 6]
    min_val = MinMaxFinder.find_min(sample_list)
    max_val = MinMaxFinder.find_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")