import math
def find_middle_index(N):
    if N <= 0:
        return None
    mid_floor = math.floor((N - 1) / 2)
    mid_ceil = math.ceil((N - 1) / 2)
    return mid_floor, mid_ceil
if __name__ == '__main__':
    list_length = 5
    floor_index, ceil_index = find_middle_index(list_length)
    print(f"List Length N: {list_length}")
    print(f"Floor Index (for 0-based indexing): {floor_index}")
    print(f"Ceiling Index (for 0-based indexing): {ceil_index}")
    list_length = 6
    floor_index, ceil_index = find_middle_index(list_length)
    print(f"\nList Length N: {list_length}")
    print(f"Floor Index (for 0-based indexing): {floor_index}")
    print(f"Ceiling Index (for 0-based indexing): {ceil_index}")