def append_list_elements(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise TypeError("Both inputs must be lists.")
    list_a.extend(list_b)
    return list_a

if __name__ == '__main__':
    try:
        list_a = [1, 2, 3]
        list_b = [4, 5, 6]
        result = append_list_elements(list_a, list_b)
        print(f"Appended list: {result}")
    except TypeError as e:
        print(e)