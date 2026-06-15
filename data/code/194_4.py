def find_longest_string(string_list):
    if not string_list:
        return None, -1
    longest_string = ""
    max_length = -1
    max_index = -1
    for index, s in enumerate(string_list):
        if len(s) > max_length:
            max_length = len(s)
            longest_string = s
            max_index = index
    return longest_string, max_index
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_string(sample_list)
    print(result)