class ArrayComparator:
    def __init__(self):
        self.arr = []

    def _validate_input(self, arr):
        if not isinstance(arr, list):
            raise ValueError("Input must be a list.")
        for item in arr:
            if not isinstance(item, (int, float)):
                raise ValueError("All elements in the list must be numbers.")

    def check_adjacent_order(self, arr):
        self._validate_input(arr)
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