def filter_list(string_list, string_to_remove):
    new_list = []
    for item in string_list:
        if item != string_to_remove:
            new_list.append(item)
    return new_list
if __name__ == '__main__':
    input_list = ["apple", "banana", "cherry", "apple", "date"]
    string_to_remove = "apple"
    result = filter_list(input_list, string_to_remove)
    print(result)