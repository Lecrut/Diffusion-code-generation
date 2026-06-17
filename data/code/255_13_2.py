def find_maximum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    maximum = data[0]
    for item in data:
        if item > maximum:
            maximum = item
    return maximum
if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718, 0.577]
    list2 = [-10.5, -5.2, -20.1]
    empty_list = []
    single_element = [42.0]
    print(f"Maximum of {list1}: {find_maximum(list1)}")
    print(f"Maximum of {list2}: {find_maximum(list2)}")
    print(f"Maximum of {empty_list}: Error")
    print(f"Maximum of {single_element}: {find_maximum(single_element)}")
    try:
        find_maximum(empty_list)
    except ValueError as e:
        print(f"Caught expected error for empty list: {e}")