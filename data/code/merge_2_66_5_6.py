def calculate_unique_weight_differences(arr1: list[int], arr2: list[int]) -> set[int]:
    return {x - y for x in arr1 for y in arr2}
if __name__ == '__main__':
    array_a = [5, 10, 3]
    array_b = [7, 4, 9]
    result = calculate_unique_weight_differences(array_a, array_b)
    print(sorted(result))