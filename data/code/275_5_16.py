def find_longest_string(strings):
    longest = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest

if __name__ == '__main__':
    sample_strings = ["hello", "world", "this", "is", "a", "test"]
    result = find_longest_string(sample_strings)
    print(result)