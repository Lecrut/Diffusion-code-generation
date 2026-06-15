import math
def find_middle_index(N):
    if N <= 0:
        return None
    middle_floor = math.floor((N - 1) / 2)
    middle_ceil = math.ceil((N - 1) / 2)
    return middle_floor, middle_ceil
if __name__ == '__main__':
    list_length = 5
    floor_index, ceil_index = find_middle_index(list_length)
    print(f"List Length N: {list_length}")
    print(f"Floor Index (N-1)/2: {floor_index}")
    print(f"Ceiling Index (N-1)/2: {ceil_index}")
    list_length = 6
    floor_index, ceil_index = find_middle_index(list_length)
    print(f"\nList Length N: {list_length}")
    print(f"Floor Index (N-1)/2: {floor_index}")
    print(f"Ceiling Index (N-1)/2: {ceil_index}")