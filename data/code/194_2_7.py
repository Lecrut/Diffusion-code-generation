def get_longest_string(string_list):
    if not string_list:
        return ""
    longest_string = max(string_list, key=len)
    return longest_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = get_longest_string(sample_list)
    print(result)