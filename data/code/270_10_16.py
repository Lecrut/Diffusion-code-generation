def remove_spaces_from_strings(string_list):
    return [s.replace(" ", "") for s in string_list]

if __name__ == '__main__':
    sample_values = ["hello world", "  python programming  ", "remove spaces"]
    result = remove_spaces_from_strings(sample_values)
    print(result)