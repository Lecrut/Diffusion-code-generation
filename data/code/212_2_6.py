class MinMaxFinder:
    def find_min_max(self, numbers):
        if not numbers:
            return None, None
        minimum = numbers[0]
        maximum = numbers[0]
        for number in numbers:
            if number < minimum:
                minimum = number
            if number > maximum:
                maximum = number
        return minimum, maximum
if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_list = [15, 3, 8, 22, 1, 10]
    minimum_val, maximum_val = finder.find_min_max(sample_list)
    print(f"The list is: {sample_list}")
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")
    sample_list_2 = [-5, 100, 0, -10]
    minimum_val_2, maximum_val_2 = finder.find_min_max(sample_list_2)
    print(f"\nThe list is: {sample_list_2}")
    print(f"Minimum value: {minimum_val_2}")
    print(f"Maximum value: {maximum_val_2}")
    empty_list = []
    minimum_val_3, maximum_val_3 = finder.find_min_max(empty_list)
    print(f"\nThe list is: {empty_list}")
    print(f"Minimum value: {minimum_val_3}")
    print(f"Maximum value: {maximum_val_3}")