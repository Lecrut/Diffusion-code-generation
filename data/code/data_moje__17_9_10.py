def get_last_item(data):
    if isinstance(data, (list, tuple, str)):
        if len(data) == 0:
            return None
        return data[-1]
    raise TypeError("Expected a list, tuple, or string")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)