class ArrayComparator:
    def check_adjacent_order(self, arr):
        if len(arr) < 2:
            return {}
        result = {}
        for i in range(len(arr) - 1):
            is_non_decreasing = arr[i] <= arr[i + 1]
            result[i] = is_non_decreasing
        return result

if __name__ == '__main__':
    sample_list_1 = [3, 5, 4, 6, 8]
    sample_list_2 = [9, 7, 5, 3, 1]
    sample_list_3 = [2, 2, 2, 2, 2]
    sample_list_4 = [10, 20, 15, 25]
    sample_list_5 = [1]

    comparator = ArrayComparator()
    
    print("Sample List 1:", comparator.check_adjacent_order(sample_list_1))
    print("Sample List 2:", comparator.check_adjacent_order(sample_list_2))
    print("Sample List 3:", comparator.check_adjacent_order(sample_list_3))
    print("Sample List 4:", comparator.check_adjacent_order(sample_list_4))
    print("Sample List 5:", comparator.check_adjacent_order(sample_list_5))