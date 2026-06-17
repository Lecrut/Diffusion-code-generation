def calculate_weight_differences(arr1: list[int], arr2: list[int]) -> set[int]:
    return {a - b for a in arr1 for b in arr2}
if __name__ == '__main__':
    weights_a = [5, 3, 8]
    weights_b = [2, 7, 4]
    result_set = calculate_weight_differences(weights_a, weights_b)
    print(result_set)