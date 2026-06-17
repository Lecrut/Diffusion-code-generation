import numpy as np
def calculate_array_difference(values: list) -> float:
    arr = np.array(values)
    return float(np.max(arr) - np.min(arr))
def calculate_list_difference(values: list) -> int:
    if len(values) != 2 or not all(isinstance(x, (int, float)) for x in values):
        raise ValueError("Input must contain exactly two numeric values.")
    return abs(int(values[0]) - int(values[1]))
def calculate_multiple_differences(numbers: list) -> dict:
    if len(numbers) < 2 or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must contain at least two numeric values.")
    diffs = []
    for i in range(len(numbers) - 1):
        diff = abs(int(numbers[i]) - int(numbers[i + 1]))
        diffs.append(diff)
    return {
        "adjacent_differences": diffs,
        "total_range": max(numbers) - min(numbers),
        "count": len(diffs)
    }
if __name__ == '__main__':
    sample_array = [5.2, 10.8, 3.4]
    print(f"Array difference: {calculate_array_difference(sample_array)}")
    pair_a = (7, 3)
    print(f"Pair difference: {calculate_list_difference(pair_a)}")
    sequence = [10, 5, 20, 8]
    result = calculate_multiple_differences(sequence)
    print(f"Differences details: {result}")