import math
def find_center_index(arr):
    if not arr:
        raise ValueError("Array cannot be empty")
    length = len(arr)
    return int(math.floor(length / 2))
if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    center_index = find_center_index(sample_array)
    print(f"Center index: {center_index}")