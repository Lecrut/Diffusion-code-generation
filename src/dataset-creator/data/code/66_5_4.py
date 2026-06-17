def calculate_weight_differences(arr1: list[int], arr2: list[int]) -> set[int]:
    return {x - y for x in arr1 for y in arr2}
if __name__ == '__main__':
    weights_a = [5, 10, 15]
    weights_b = [3, 7, 9]
    result = calculate_weight_differences(weights_a, weights_b)
    print(sorted(result))