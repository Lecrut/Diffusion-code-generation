def find_maximum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    if isinstance(data[0], list):
        return max(find_maximum(item) for item in data)
    else:
        return max(data)

if __name__ == '__main__':
    nested_list = [3.14, 1.618, [2.718, 0.577], [-10.5, -5.2, [-20.1, -1.9]]]
    empty_list = []
    single_element = [42.0]

    try:
        max_nested = find_maximum(nested_list)
        print(f"Maximum of {nested_list}: {max_nested}")
    except ValueError as e:
        print(e)

    try:
        max_empty = find_maximum(empty_list)
        print(f"Maximum of {empty_list}: {max_empty}")
    except ValueError as e:
        print(e)

    max_single = find_maximum(single_element)
    print(f"Maximum of {single_element}: {max_single}")