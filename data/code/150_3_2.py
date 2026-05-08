def filter_list(string_list, string_to_remove):
    new_list = []
    for item in string_list:
        if item != string_to_remove:
            new_list.append(item)
    return new_list
if __name__ == '__main__':
    input_list = ["apple", "banana", "cherry", "apple", "date"]
    remove_string = "apple"
    result = filter_list(input_list, remove_string)
    print(result)