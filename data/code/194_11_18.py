def find_longest_string(strings):
    if not strings:
        return ""
    
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_string(sample_strings)
    print(result)