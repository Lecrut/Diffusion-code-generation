class ArrayComparator:
    def compare_adjacent_pairs(self, arr):
        result = []
        n = len(arr)
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                result.append(arr[i])
            else:
                result.append(arr[i + 1])
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_array_1 = [3, 1, 4, 1, 5, 9]
    sample_array_2 = [10, 8, 12, 6, 14, 2]
    sample_array_3 = [7, 7, 7, 7, 7]
    sample_array_4 = [5, 4, 3, 2, 1]

    result_1 = comparator.compare_adjacent_pairs(sample_array_1)
    print("Sample 1:", result_1)

    result_2 = comparator.compare_adjacent_pairs(sample_array_2)
    print("Sample 2:", result_2)

    result_3 = comparator.compare_adjacent_pairs(sample_array_3)
    print("Sample 3:", result_3)

    result_4 = comparator.compare_adjacent_pairs(sample_array_4)
    print("Sample 4:", result_4)