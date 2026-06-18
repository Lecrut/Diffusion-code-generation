def calculate_unique_weight_differences(arr1: list[int], arr2: list[int]) -> set[int]:
    return {a - b for a in arr1 for b in arr2}
if __name__ == '__main__':
    input_array_1 = [5, 3, 8]
    input_array_2 = [2, 7, 4]
    result_set = calculate_unique_weight_differences(input_array_1, input_array_2)
    print(result_set)