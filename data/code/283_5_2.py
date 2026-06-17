def filter_numeric(data):
    result = []
    for item in data:
        if isinstance(item, (int, float)):
            result.append(item)
    return result
if __name__ == '__main__':
    mixed_list = [1, "hello", 3.14, True, 5, "world", 7.0, None, [1, 2]]
    numeric_list = filter_numeric(mixed_list)
    print(numeric_list)