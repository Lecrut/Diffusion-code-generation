class MinMaxFinder:
    def find_min_max(self, data):
        if not data:
            return None, None
        minimum = data[0]
        maximum = data[0]
        for num in data:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
        return minimum, maximum
if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_list = [15, 3, 8, 22, 1, 10]
    minimum_val, maximum_val = finder.find_min_max(sample_list)
    print(f"The list is: {sample_list}")
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")
    sample_list_2 = [-5, 100, 0, -50]
    minimum_val_2, maximum_val_2 = finder.find_min_max(sample_list_2)
    print(f"\nThe list is: {sample_list_2}")
    print(f"Minimum value: {minimum_val_2}")
    print(f"Maximum value: {maximum_val_2}")