def remove_spaces(list_of_strings):
    new_list = []
    for s in list_of_strings:
        new_list.append(s.replace(' ', ''))
    return new_list
if __name__ == '__main__':
    sample_list = ["hello world", "  python programming ", "a b c"]
    result = remove_spaces(sample_list)
    print(result)