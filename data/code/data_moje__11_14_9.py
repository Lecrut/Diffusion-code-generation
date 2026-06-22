def get_last_item(items):
    if not isinstance(items, list):
        raise TypeError("Input must be a list")
    if len(items) == 0:
        raise IndexError("Cannot get the last item of an empty list")
    return items[-1]

if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_item(sample_list))
    print(get_last_item(["a", "b", "c"]))
    try:
        get_last_item(123)
    except TypeError as e:
        print(e)
    try:
        get_last_item([])
    except IndexError as e:
        print(e)