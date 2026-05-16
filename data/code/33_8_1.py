def remove_spaces(list_of_strings):
    new_list = []
    for s in list_of_strings:
        new_list.append(s.replace(' ', ''))
    return new_list
if __name__ == '__main__':
    input_list = ["hello world", "  python programming  ", "a b c d"]
    result = remove_spaces(input_list)
    print(result)