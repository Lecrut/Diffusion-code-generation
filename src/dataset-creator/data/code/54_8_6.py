import math
def find_center_mark(arr):
    n = len(arr)
    if n == 0:
        return None
    mid_index = n // 2
    result = [arr[mid_index]]
    if n % 2 == 0:
        left_idx = (n // 2) - 1
        right_idx = (n // 2) + 1
        if len(arr) > 1 and mid_index < n - 1:
            result.append(arr[mid_index])
    return arr[n // 2]
if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    center_value = find_center_mark(sample_array)
    print(f"Center mark of {sample_array}:")
    if isinstance(center_value, list):
        for item in center_value:
            print(item)
    else:
        print(center_value)