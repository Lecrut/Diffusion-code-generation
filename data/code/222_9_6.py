def find_minimum(iterable):
    if not iterable:
        raise ValueError("Iterable cannot be empty")
    min_value = iterable[0]
    for item in iterable[1:]:
        if item < min_value:
            min_value = item
    return min_value
if __name__ == '__main__':
    list1 = [5, 2, 9, 1, 7]
    tuple2 = (100, 45, 88, 3)
    empty_list = []
    single_item = [42]
    print(f"Minimum of {list1}: {find_minimum(list1)}")
    print(f"Minimum of {tuple2}: {find_minimum(tuple2)}")
    try:
        find_minimum(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")
    print(f"Minimum of {single_item}: {find_minimum(single_item)}")