def filter_string_list(data, target):
    return [item for item in data if item != target]

if __name__ == '__main__':
    initial_list = ["apple", "banana", "cherry", "date", "banana"]
    target_string = "banana"
    filtered_list = filter_string_list(initial_list, target_string)
    print(filtered_list)