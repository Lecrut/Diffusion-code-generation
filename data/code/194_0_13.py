def find_longest_string(strings):
    if not strings:
        return None
    longest = max(strings, key=len)
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    result = find_longest_string(sample_strings)
    print(result)