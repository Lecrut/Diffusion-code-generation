import math
def find_midpoint(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    for item in arr:
        try:
            float(item)
        except (ValueError, TypeError):
            raise ValueError("All elements in the array must be numeric.")
    n = len(arr)
    if n == 0:
        return None
    mid_index = math.floor(n / 2)
    return (mid_index, arr[mid_index])
if __name__ == '__main__':
    sample_array = [1.5, 3.0, 4.2]
    result = find_midpoint(sample_array)
    print(result)