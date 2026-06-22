class ArrayComparator:
    def check_adjacent_order(self, arr):
        if len(arr) < 2:
            return {}
        
        result = {}
        for i in range(len(arr) - 1):
            result[i] = arr[i] <= arr[i + 1]
        
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_array_1 = [3, 5, 2, 6, 8, 7]
    sample_array_2 = [10, 20, 30, 40, 50]
    sample_array_3 = [1, 2, 3, 3, 2]
    sample_array_4 = [5, 4, 3, 2, 1]
    sample_array_5 = [7, 8, 9, 10, 11]

    print("Sample Array 1:", comparator.check_adjacent_order(sample_array_1))
    print("Sample Array 2:", comparator.check_adjacent_order(sample_array_2))
    print("Sample Array 3:", comparator.check_adjacent_order(sample_array_3))
    print("Sample Array 4:", comparator.check_adjacent_order(sample_array_4))
    print("Sample Array 5:", comparator.check_adjacent_order(sample_array_5))