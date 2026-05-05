class ArrayComparator:
    def check_adjacent_order(self, arr):
        result = {}
        n = len(arr)
        for i in range(n - 1):
            pair = (i, i + 1)
            is_non_decreasing = arr[i] <= arr[i + 1]
            result[pair] = is_non_decreasing
        return result
if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_array_1 = [1, 3, 2, 5, 4]
    sample_array_2 = [10, 20, 30, 15, 5]
    sample_array_3 = [1, 1, 2, 2, 3]
    sample_array_4 = [5, 4, 3, 2, 1]
    result_1 = comparator.check_adjacent_order(sample_array_1)
    print("Sample 1:", result_1)
    result_2 = comparator.check_adjacent_order(sample_array_2)
    print("Sample 2:", result_2)
    result_3 = comparator.check_adjacent_order(sample_array_3)
    print("Sample 3:", result_3)
    result_4 = comparator.check_adjacent_order(sample_array_4)
    print("Sample 4:", result_4)