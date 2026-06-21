def get_last_item(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) == 0:
        raise IndexError("Cannot get the last item of an empty list")
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
    except IndexError as e:
        print(e)