class ArrayComparator:
    def check_adjacent_order(self, arr):
        result = {}
        for i in range(len(arr) - 1):
            is_non_decreasing = arr[i] <= arr[i + 1]
            result[i] = is_non_decreasing
        return result

if __name__ == '__main__':
    sample_list_1 = [3, 5, 2, 8, 6, 7]
    sample_list_2 = [9, 8, 7, 6, 5]
    sample_list_3 = [1, 1, 1, 1, 1]
    sample_list_4 = [10, 20, 30, 40, 50]
    sample_list_5 = [5, 3, 8, 6, 7]

    comparator = ArrayComparator()

    print(comparator.check_adjacent_order(sample_list_1))
    print(comparator.check_adjacent_order(sample_list_2))
    print(comparator.check_adjacent_order(sample_list_3))
    print(comparator.check_adjacent_order(sample_list_4))
    print(comparator.check_adjacent_order(sample_list_5))