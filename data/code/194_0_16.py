def find_longest_string(string_list):
    if not string_list:
        return None
    longest = max(string_list, key=len)
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    result = find_longest_string(sample_strings)
    print(result)