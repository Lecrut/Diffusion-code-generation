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
    print(f"List length: {list_length}")
    print(f"Floor middle index: {floor_idx}")
    print(f"Ceiling middle index: {ceil_idx}")
    list_length = 6
    floor_idx, ceil_idx = find_middle_index(list_length)
    print(f"\nList length: {list_length}")
    print(f"Floor middle index: {floor_idx}")
    print(f"Ceiling middle index: {ceil_idx}")