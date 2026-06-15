def uppercase_strings(string_list):
    uppercase_list = []
    for s in string_list:
        uppercase_list.append(s.upper())
    return uppercase_list
if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "scripting"]
    result = uppercase_strings(sample_strings)
    for upper_string in result:
        print(upper_string)