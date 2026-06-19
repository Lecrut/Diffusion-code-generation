class ArrayComparator:
    def check_adjacent_order(self, arr):
        result = {}
        for i in range(len(arr) - 1):
            is_non_decreasing = arr[i] <= arr[i + 1]
            result[i] = is_non_decreasing
        return result

if __name__ == '__main__':
    sample_list_1 = [3, 5, 4, 6, 7]
    sample_list_2 = [9, 8, 7, 6, 5]
    sample_list_3 = [2, 2, 3, 3, 4]
    sample_list_4 = [10, 20, 20, 30]
    sample_list_5 = [5, 5, 5, 5]
    sample_list_6 = [1]
    sample_list_7 = []

    comparator = ArrayComparator()

    print(f"Sample List 1: {comparator.check_adjacent_order(sample_list_1)}")
    print(f"Sample List 2: {comparator.check_adjacent_order(sample_list_2)}")
    print(f"Sample List 3: {comparator.check_adjacent_order(sample_list_3)}")
    print(f"Sample List 4: {comparator.check_adjacent_order(sample_list_4)}")
    print(f"Sample List 5: {comparator.check_adjacent_order(sample_list_5)}")
    print(f"Sample List 6: {comparator.check_adjacent_order(sample_list_6)}")
    print(f"Sample List 7: {comparator.check_adjacent_order(sample_list_7)}")