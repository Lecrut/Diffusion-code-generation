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
    sample_array1 = [1, 3, 2, 5, 4]
    sample_array2 = [10, 20, 30, 15, 5]
    sample_array3 = [1, 2, 3, 4, 5]
    sample_array4 = [5, 4, 3, 2, 1]
    result1 = comparator.check_adjacent_order(sample_array1)
    print(f"Array: {sample_array1}")
    print(f"Result: {result1}")
    result2 = comparator.check_adjacent_order(sample_array2)
    print(f"Array: {sample_array2}")
    print(f"Result: {result2}")
    result3 = comparator.check_adjacent_order(sample_array3)
    print(f"Array: {sample_array3}")
    print(f"Result: {result3}")
    result4 = comparator.check_adjacent_order(sample_array4)
    print(f"Array: {sample_array4}")
    print(f"Result: {result4}")