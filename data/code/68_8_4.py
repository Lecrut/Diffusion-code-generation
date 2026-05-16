def calculate_differences(list1: list[float], list2: list[float]) -> list[float]:
    if len(list1) != len(list2):
        raise ValueError("Input lists must have the same length")
    differences = []
    for a, b in zip(list1, list2):
        differences.append(a - b)
    return differences
if __name__ == '__main__':
    list_a = [1.0, 2.5, 3.14, 4.0]
    list_b = [0.5, 2.0, 3.0, 3.0]
    result = calculate_differences(list_a, list_b)
    print(result)