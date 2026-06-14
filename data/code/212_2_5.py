class MinMaxFinder:
    def find_min_max(self, data):
        if not data:
            return None, None
        minimum = data[0]
        maximum = data[0]
        for x in data:
            if x < minimum:
                minimum = x
            if x > maximum:
                maximum = x
        return minimum, maximum
if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_list = [15, 3, 8, 22, 1, 40]
    minimum_val, maximum_val = finder.find_min_max(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")
    sample_list_2 = [-5, 10, 0, -100]
    minimum_val_2, maximum_val_2 = finder.find_min_max(sample_list_2)
    print(f"\nList: {sample_list_2}")
    print(f"Minimum value: {minimum_val_2}")
    print(f"Maximum value: {maximum_val_2}")