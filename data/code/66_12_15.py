def compare_adjacent_pairs(arr):
    result = []
    n = len(arr)
    for i in range(n - 1):
        larger_value = max(arr[i], arr[i + 1])
        result.append(larger_value)
    return result

if __name__ == '__main__':
    sample_array1 = [1, 3, 2, 5, 4]
    sample_array2 = [10, 20, 30, 15, 5]
    sample_array3 = [1, 2, 3, 4, 5]
    sample_array4 = [5, 4, 3, 2, 1]

    result1 = compare_adjacent_pairs(sample_array1)
    print("Array:", sample_array1)
    print("Larger Values from Adjacent Pairs:", result1)

    result2 = compare_adjacent_pairs(sample_array2)
    print("Array:", sample_array2)
    print("Larger Values from Adjacent Pairs:", result2)

    result3 = compare_adjacent_pairs(sample_array3)
    print("Array:", sample_array3)
    print("Larger Values from Adjacent Pairs:", result3)

    result4 = compare_adjacent_pairs(sample_array4)
    print("Array:", sample_array4)
    print("Larger Values from Adjacent Pairs:", result4)