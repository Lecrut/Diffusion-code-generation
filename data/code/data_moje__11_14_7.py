def get_last_item(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if not data:
        raise IndexError("List is empty")
    return data[-1]

if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_item(sample_list))
    empty_list = []
    try:
        print(get_last_item(empty_list))
    except IndexError as e:
        print(e)
    non_list = "string"
    try:
        print(get_last_item(non_list))
    except TypeError as e:
        print(e)