import math
def find_center_index(arr):
    if not arr:
        raise ValueError("Array cannot be empty.")
    n = len(arr)
    mid = n // 2
    return mid
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    center_index = find_center_index(sample_data)
    print(f"Center index: {center_index}")