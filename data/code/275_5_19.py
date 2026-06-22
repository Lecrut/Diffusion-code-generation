def find_longest_string(strings):
    if not strings:
        return ""
    
    longest = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest):
            longest = string
    
    return longest

if __name__ == '__main__':
    sample_strings = ["python", "java", "csharp", "javascript"]
    result = find_longest_string(sample_strings)
    print(result)