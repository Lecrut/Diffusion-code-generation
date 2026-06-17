def calculate_unique_weight_differences(array1: list[int], array2: list[int]) -> set[int]:
    return {x - y for x in array1 for y in array2}
if __name__ == '__main__':
    weights_a = [5, 3, 8]
    weights_b = [4, 6, 9]
    result_set = calculate_unique_weight_differences(weights_a, weights_b)
    print(sorted(result_set))