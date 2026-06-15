class MinMaxFinder:
    def get_min_max(self, data_list):
        if not data_list:
            return None, None
        minimum = data_list[0]
        maximum = data_list[0]
        for item in data_list:
            if item < minimum:
                minimum = item
            if item > maximum:
                maximum = item
        return minimum, maximum
if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_data = [15, 3, 88, 42, 9, 55]
    min_val, max_val = finder.get_min_max(sample_data)
    print(f"Data: {sample_data}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")
    sample_data_2 = [-10, 5, 0, -20, 30]
    min_val_2, max_val_2 = finder.get_min_max(sample_data_2)
    print(f"\nData: {sample_data_2}")
    print(f"Minimum value: {min_val_2}")
    print(f"Maximum value: {max_val_2}")
    empty_data = []
    min_val_3, max_val_3 = finder.get_min_max(empty_data)
    print(f"\nData: {empty_data}")
    print(f"Minimum value: {min_val_3}")
    print(f"Maximum value: {max_val_3}")