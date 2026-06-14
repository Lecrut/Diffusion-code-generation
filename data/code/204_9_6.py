import math
def find_middle_index(N):
    if N <= 0:
        return None
    middle_floor = math.floor((N - 1) / 2)
    middle_ceiling = math.ceil((N - 1) / 2)
    return middle_floor, middle_ceiling
if __name__ == '__main__':
    list_length = 5
    floor_index, ceiling_index = find_middle_index(list_length)
    print(f"List Length: {list_length}")
    print(f"Floor Index: {floor_index}")
    print(f"Ceiling Index: {ceiling_index}")
    list_length = 6
    floor_index, ceiling_index = find_middle_index(list_length)
    print(f"\nList Length: {list_length}")
    print(f"Floor Index: {floor_index}")
    print(f"Ceiling Index: {ceiling_index}")