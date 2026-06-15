def find_minimum(iterable):
    if not iterable:
        raise ValueError("Iterable cannot be empty")
    current_min = iterable[0]
    for item in iterable[1:]:
        if item < current_min:
            current_min = item
    return current_min
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    tuple2 = (100, 45, 33, 99)
    empty_list = []
    single_element = [42]
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {tuple2}: {find_minimum(tuple2)}")
    try:
        find_minimum(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")
    print(f"Minimum of {single_element}: {find_minimum(single_element)}")