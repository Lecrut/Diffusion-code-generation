import math
def find_midpoint(arr: list[int]) -> int | None:
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    n = len(arr)
    if n == 0:
        return None
    try:
        mid_index = math.floor(n / 2)
        return arr[mid_index]
    except IndexError as e:
        raise RuntimeError(f"Index out of range. {e}")
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = find_midpoint(sample_data)
    print(result)