class ArrayComparator:
    def check_adjacent_order(self, arr):
        result = {}
        for i in range(len(arr) - 1):
            is_non_decreasing = arr[i] <= arr[i + 1]
            result[i] = is_non_decreasing
        return result

if __name__ == '__main__':
    sample_list_8 = [3, 5, 4, 6, 7]
    sample_list_9 = [2, 2, 2, 2]
    sample_list_10 = [9, 8, 7]
    sample_list_11 = [1]
    sample_list_12 = []

    comparator = ArrayComparator()

    print("Sample List 8:", comparator.check_adjacent_order(sample_list_8))
    print("Sample List 9:", comparator.check_adjacent_order(sample_list_9))
    print("Sample List 10:", comparator.check_adjacent_order(sample_list_10))
    print("Sample List 11:", comparator.check_adjacent_order(sample_list_11))
    print("Sample List 12:", comparator.check_adjacent_order(sample_list_12))