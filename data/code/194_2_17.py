def find_longest_string(string_list):
    if not string_list:
        return ""
    longest_str = ""
    for item in string_list:
        if len(item) > len(longest_str):
            longest_str = item
    return longest_str

if __name__ == '__main__':
    sample_values = ["dog", "elephant", "cat", "hippopotamus", "mouse"]
    result = find_longest_string(sample_values)
    print(result)