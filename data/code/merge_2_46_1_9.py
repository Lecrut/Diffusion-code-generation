def absolute_difference(arr1: list[float], arr2: list[float]) -> list[float]:
    if len(arr1) != len(arr2):
        raise ValueError("Input arrays must have the same length.")
    result = []
    for i in range(len(arr1)):
        diff = abs(arr1[i] - arr2[i])
        result.append(diff)
    return result
if __name__ == '__main__':
    sample_array_1 = [3.5, 7.0, 9.2, 4.8]
    sample_array_2 = [1.0, 6.5, 3.0, 2.1]
    try:
        diff_result = absolute_difference(sample_array_1, sample_array_2)
        print(diff_result)
    except ValueError as e:
        print(f"Error: {e}")