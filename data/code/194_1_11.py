def find_longest_list_item(string_list):
    if not string_list:
        return ""
    longest_string = string_list[0]
    for s in string_list:
        if len(s) > len(longest_string):
            longest_string = s
    return longest_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_list_item(sample_list)
    print(result)