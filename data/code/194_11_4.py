def find_longest_string(strings):
    if not strings:
        return ""
    
    longest = max(strings, key=len)
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_string(sample_strings)
    print(result)