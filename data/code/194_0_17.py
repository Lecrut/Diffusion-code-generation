def find_longest_string(string_list):
    return max(string_list, key=len) if string_list else None

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_string(sample_strings)
    print(result)