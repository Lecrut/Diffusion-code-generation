def uppercase_list(string_list):
    uppercase_strings = []
    for s in string_list:
        uppercase_strings.append(s.upper())
    return uppercase_strings
if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "scripting"]
    result = uppercase_list(sample_strings)
    for upper_string in result:
        print(upper_string)