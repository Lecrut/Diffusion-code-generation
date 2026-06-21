def find_longest_string(strings):
    longest = None
    for string in strings:
        if longest is None or len(string) > len(longest):
            longest = string
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))