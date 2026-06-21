def find_longest_string(string_list):
    if not string_list:
        return None
    MAX_LENGTH = 0
    LONGEST_STRING = ""
    for s in string_list:
        if len(s) > MAX_LENGTH:
            MAX_LENGTH = len(s)
            LONGEST_STRING = s
    return LONGEST_STRING

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_string(sample_strings)
    print(result)