def find_longest_string(strings):
    longest = None
    for s in strings:
        if longest is None or len(s) > len(longest):
            longest = s
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))