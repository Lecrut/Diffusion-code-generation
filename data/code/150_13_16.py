def filter_string_from_list(data, target):
    return [item for item in data if item != target]

if __name__ == '__main__':
    initial_strings = ["apple", "banana", "cherry", "date"]
    target_string = "banana"
    filtered_list = filter_string_from_list(initial_strings, target_string)
    print(filtered_list)