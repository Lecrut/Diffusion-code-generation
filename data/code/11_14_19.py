def get_last_item(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if not data:
        raise ValueError("List cannot be empty")
    return data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)
    try:
        get_last_item("not a list")
    except TypeError as e:
        print(e)
    try:
        get_last_item([])
    except ValueError as e:
        print(e)