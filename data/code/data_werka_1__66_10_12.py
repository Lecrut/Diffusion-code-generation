class ArrayComparator:
    def __init__(self):
        self._validate_input = lambda arr: (isinstance(arr, list) and all(isinstance(item, (int, float)) for item in arr))

    def check_adjacent_order(self, arr):
        if not self._validate_input(arr):
            raise ValueError("Input must be a list of numbers.")
        result = {}
        for i in range(len(arr) - 1):
            result[i] = arr[i] <= arr[i + 1]
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [5, 4, 3, 2, 1]
    sample_list_3 = [1, 3, 2, 5, 4]
    sample_list_4 = [10, 20, 30]
    sample_list_5 = [7, 7, 8, 9]
    sample_list_6 = [1]
    sample_list_7 = []

    print(comparator.check_adjacent_order(sample_list_1))
    print(comparator.check_adjacent_order(sample_list_2))
    print(comparator.check_adjacent_order(sample_list_3))
    print(comparator.check_adjacent_order(sample_list_4))
    print(comparator.check_adjacent_order(sample_list_5))
    print(comparator.check_adjacent_order(sample_list_6))
    print(comparator.check_adjacent_order(sample_list_7))