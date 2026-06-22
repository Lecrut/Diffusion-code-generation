def find_maximum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    if isinstance(data[0], list):
        return max(find_maximum(item) for item in data)
    return max(data)

if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718, 0.577]
    list2 = [-10.5, -5.2, -20.1]
    nested_list = [list1, list2, [42.0, 3.14]]
    empty_list = []
    try:
        max1 = find_maximum(list1)
        print(f"Maximum of {list1}: {max1}")
        max2 = find_maximum(list2)
        print(f"Maximum of {list2}: {max2}")
        max_nested = find_maximum(nested_list)
        print(f"Maximum in nested list: {max_nested}")
        find_maximum(empty_list)
    except ValueError as e:
        print(e)