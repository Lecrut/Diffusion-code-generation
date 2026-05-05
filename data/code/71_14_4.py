def find_middle_element(data):
    n = len(data)
    if n == 0:
        return None
    middle_index = n // 2
    if n % 2 == 1:
        return data[middle_index]
    else:
        return data[middle_index]
if __name__ == '__main__':
    list_odd = [1, 2, 3, 4, 5]
    list_even = [10, 20, 30, 40]
    list_single = [99]
    list_empty = []
    print(f"Middle element of {list_odd}: {find_middle_element(list_odd)}")
    print(f"Middle element of {list_even}: {find_middle_element(list_even)}")
    print(f"Middle element of {list_single}: {find_middle_element(list_single)}")
    print(f"Middle element of {list_empty}: {find_middle_element(list_empty)}")