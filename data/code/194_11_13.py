def find_longest_string(string_list):
    if not string_list:
        return ""
    longest = string_list[0]
    for s in string_list:
        if len(s) > len(longest):
            longest = s
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_string(sample_strings)
    print(result)