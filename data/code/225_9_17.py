class MinMaxFinder:
    @staticmethod
    def find_min_max(data):
        if not data:
            return None, None
        min_val = data[0]
        max_val = data[0]
        for number in data[1:]:
            if number < min_val:
                min_val = number
            if number > max_val:
                max_val = number
        return min_val, max_val

if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_data = [10, 5, 20, -3, 15, 8, 25, -10]
    min_result, max_result = finder.find_min_max(sample_data)
    print(f"Minimum value: {min_result}")
    print(f"Maximum value: {max_result}")
    sample_data_large = [1000, -500, 999, 0, 5000, -100]
    min_result_large, max_result_large = finder.find_min_max(sample_data_large)
    print(f"Minimum value (large): {min_result_large}")
    print(f"Maximum value (large): {max_result_large}")