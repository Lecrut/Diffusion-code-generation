def get_last_item(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) == 0:
        raise IndexError("List is empty")
    return data[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)

    another_list = ['apple', 'banana', 'cherry']
    result2 = get_last_item(another_list)
    print(result2)

    single_item_list = [42]
    result3 = get_last_item(single_item_list)
    print(result3)

    try:
        get_last_item("not a list")
    except TypeError as e:
        print(str(e))

    try:
        get_last_item([])
    except IndexError as e:
        print(str(e))