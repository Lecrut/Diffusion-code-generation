def get_last_item(input_data):
    if not isinstance(input_data, list):
        raise TypeError("Input must be a list")
    if len(input_data) == 0:
        raise IndexError("List is empty")
    return input_data[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)
    another_list = ['a', 'b', 'c']
    result2 = get_last_item(another_list)
    print(result2)
    try:
        get_last_item("not a list")
    except TypeError as e:
        print(e)
    try:
        get_last_item([])
    except IndexError as e:
        print(e)