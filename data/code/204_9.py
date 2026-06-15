import math
def find_middle_index(N):
    if N % 2 == 1:
        middle_index = N // 2
    else:
        floor_index = N // 2 - 1
        ceiling_index = N // 2
        middle_index = (floor_index + ceiling_index) // 2
    return middle_index
if __name__ == '__main__':
    list_length_odd = 5
    result_odd = find_middle_index(list_length_odd)
    print(f"List Length: {list_length_odd}")
    print(f"Middle Index (Floor/Ceiling consideration): {result_odd}")
    list_length_even = 6
    result_even = find_middle_index(list_length_even)
    print(f"\nList Length: {list_length_even}")
    print(f"Middle Index (Floor/Ceiling consideration): {result_even}")