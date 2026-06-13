def find_longest_string(string_list):
    if not string_list:
        return None
    longest_string = ""
    max_length = -1
    for s in string_list:
        if len(s) > max_length:
            max_length = len(s)
            longest_string = s
    return longest_string
if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result = find_longest_string(sample_strings)
    print(result)