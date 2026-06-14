def find_minimum(iterable):
    if not iterable:
        raise ValueError("Input iterable cannot be empty")
    minimum = iterable[0]
    for item in iterable[1:]:
        if item < minimum:
            minimum = item
    return minimum
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    tuple2 = (100, 45, 72, 33)
    empty_list = []
    single_element = [42]
    print(f"Minimum in {list1}: {find_minimum(list1)}")
    print(f"Minimum in {tuple2}: {find_minimum(tuple2)}")
    try:
        find_minimum(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")
    print(f"Minimum in {single_element}: {find_minimum(single_element)}")