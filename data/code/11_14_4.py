def get_last_item(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if not data:
        raise IndexError("List is empty")
    return data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)