def separate_data(data):
    strings = []
    numbers = []
    for item in data:
        if isinstance(item, str):
            strings.append(item)
        elif isinstance(item, (int, float)):
            numbers.append(item)
    return strings, numbers
if __name__ == '__main__':
    sample_tuple = (10, "hello", 3.14, "world", 5, True)
    strings_list, numbers_list = separate_data(sample_tuple)
    print("Strings:", strings_list)
    print("Numbers:", numbers_list)