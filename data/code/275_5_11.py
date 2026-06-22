def find_longest_string(strings):
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest

if __name__ == '__main__':
    sample_strings = ["programming", "is", "fun", "and", "challenging"]
    result = find_longest_string(sample_strings)
    print(result)