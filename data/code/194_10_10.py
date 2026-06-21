def find_longest_string(strings):
    if not strings:
        return None
    
    longest = strings[0]
    
    for string in strings[1:]:
        if len(string) > len(longest):
            longest = string
            
    return longest

if __name__ == '__main__':
    sample_strings = ["hello", "world", "this", "is", "a", "test"]
    print(find_longest_string(sample_strings))