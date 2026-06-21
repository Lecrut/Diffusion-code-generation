def find_longest_string(string_list):
    if not string_list:
        return None
    longest = ""
    for s in string_list:
        if len(s) > len(longest):
            longest = s
    return longest

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result = find_longest_string(sample_list)
    print(result)