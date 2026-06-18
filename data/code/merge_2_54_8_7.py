import sys
def find_center_mark(arr):
    if len(arr) % 2 != 0:
        raise ValueError("Array length must be even to define a center mark.")
    mid_index = len(arr) // 2
    return arr[mid_index - 1], arr[mid_index]
if __name__ == '__main__':
    sample_array = [1, 3, 5, 7, 9, 11]
    center_pair = find_center_mark(sample_array)
    print(f"Center mark pair: {center_pair}")