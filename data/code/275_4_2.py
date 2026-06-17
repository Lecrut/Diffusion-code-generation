def separate_data(data_tuple):
    strings = []
    numbers = []
    for item in data_tuple:
        if isinstance(item, str):
            strings.append(item)
        elif isinstance(item, (int, float)):
            numbers.append(item)
    return strings, numbers
if __name__ == '__main__':
    sample_data = (10, "hello", 3.14, "world", 5, True, "test")
    strings_list, numbers_list = separate_data(sample_data)
    print("Strings:", strings_list)
    print("Numbers:", numbers_list)