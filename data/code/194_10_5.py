def find_longest_string(strings):
    if not strings:
        raise ValueError("Input list cannot be empty")
    
    longest = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest):
            longest = string
    
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))