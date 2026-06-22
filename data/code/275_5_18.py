def find_longest_string(strings):
    if not strings:
        return ""
    longest = strings[0]
    for s in strings[1:]:
        if len(s) > len(longest):
            longest = s
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))