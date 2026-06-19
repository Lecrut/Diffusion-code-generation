class ArrayComparator:
    @staticmethod
    def check_adjacent_order(arr):
        if len(arr) < 2:
            return {}
        result = {}
        for i in range(len(arr) - 1):
            result[i] = arr[i] <= arr[i + 1]
        return result

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [5, 4, 3, 2, 1]
    sample_list_3 = [1, 3, 2, 5, 4]
    sample_list_4 = [10, 20, 30]
    sample_list_5 = [7, 7, 8, 9]
    sample_list_6 = [1]
    sample_list_7 = []

    comparator = ArrayComparator()

    print("Sample List 1:", comparator.check_adjacent_order(sample_list_1))
    print("Sample List 2:", comparator.check_adjacent_order(sample_list_2))
    print("Sample List 3:", comparator.check_adjacent_order(sample_list_3))
    print("Sample List 4:", comparator.check_adjacent_order(sample_list_4))
    print("Sample List 5:", comparator.check_adjacent_order(sample_list_5))
    print("Sample List 6:", comparator.check_adjacent_order(sample_list_6))
    print("Sample List 7:", comparator.check_adjacent_order(sample_list_7))