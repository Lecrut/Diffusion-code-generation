def compare_adjacent_pairs(arr):
    result = []
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            result.append(arr[i])
        else:
            result.append(arr[i + 1])
    return result

if __name__ == '__main__':
    sample_array1 = [1, 3, 2, 5, 4]
    sample_array2 = [10, 20, 30, 15, 5]
    sample_array3 = [1, 2, 3, 4, 5]
    sample_array4 = [5, 4, 3, 2, 1]

    result1 = compare_adjacent_pairs(sample_array1)
    result2 = compare_adjacent_pairs(sample_array2)
    result3 = compare_adjacent_pairs(sample_array3)
    result4 = compare_adjacent_pairs(sample_array4)

    print("Result for sample_array1:", result1)
    print("Result for sample_array2:", result2)
    print("Result for sample_array3:", result3)
    print("Result for sample_array4:", result4)