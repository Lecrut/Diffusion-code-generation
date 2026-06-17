import sys
def compute_absolute_difference(arr1: list, arr2: list) -> tuple[list[int], str]:
    if len(arr1) != len(arr2):
        return [], "Error: Arrays must have the same length."
    result = []
    for a, b in zip(arr1, arr2):
        try:
            diff = abs(a - b)
            result.append(int(diff))
        except TypeError as e:
            return [], f"Error: Cannot compute difference. {str(e)}"
    return result, "Success."
if __name__ == '__main__':
    sample_arr1 = [5, 3, 8]
    sample_arr2 = [2, 7, 4]
    diff_list, message = compute_absolute_difference(sample_arr1, sample_arr2)
    print(f"Result: {diff_list}")
    print(f"Status: {message}")