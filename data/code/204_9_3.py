import math
def find_middle_index(N):
    if N <= 0:
        return None
    floor_index = math.floor((N - 1) / 2)
    ceiling_index = math.ceil((N - 1) / 2)
    return floor_index, ceiling_index
if __name__ == '__main__':
    list_length = 5
    floor_idx, ceil_idx = find_middle_index(list_length)
    print(f"List Length N: {list_length}")
    print(f"Floor Index: {floor_idx}")
    print(f"Ceiling Index: {ceil_idx}")
    list_length = 6
    floor_idx, ceil_idx = find_middle_index(list_length)
    print(f"\nList Length N: {list_length}")
    print(f"Floor Index: {floor_idx}")
    print(f"Ceiling Index: {ceil_idx}")