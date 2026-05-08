def filter_strings(string_list, string_to_remove):
    new_list = []
    for s in string_list:
        if s != string_to_remove:
            new_list.append(s)
    return new_list
if __name__ == '__main__':
    input_list = ["apple", "banana", "cherry", "apple", "date"]
    remove_string = "apple"
    result = filter_strings(input_list, remove_string)
    print(result)