def absolute_difference(arr1: list, arr2: list) -> int:
    if len(arr1) != len(arr2):
        raise ValueError("Input arrays must have the same length.")
    total_diff = 0
    for i in range(len(arr1)):
        diff = abs(arr1[i] - arr2[i])
        total_diff += diff
    return total_diff
if __name__ == '__main__':
    array_a = [3, 5, 7, 9]
    array_b = [10, 2, 4, 8]
    try:
        result = absolute_difference(array_a, array_b)
        print(f"Total Absolute Difference: {result}")
    except ValueError as e:
        print(f"Error: {e}")