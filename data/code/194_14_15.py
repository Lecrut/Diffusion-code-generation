def find_longest_string(list_of_strings):
    max_length = -1
    longest_string = ""
    for string in list_of_strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
    return longest_string

if __name__ == '__main__':
    sample_data = [
        "apple",
        "banana",
        "cherry"
    ]
    result = find_longest_string(sample_data)
    print(result)