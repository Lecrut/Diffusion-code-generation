def get_last_item(input_data):
    if not isinstance(input_data, list):
        raise TypeError("Input must be a list")
    if len(input_data) == 0:
        return None
    return input_data[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_item(sample_list))
    empty_list = []
    print(get_last_item(empty_list))
    try:
        get_last_item("not a list")
    except TypeError as e:
        print(e)