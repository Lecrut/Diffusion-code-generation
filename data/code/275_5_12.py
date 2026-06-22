def is_valid_string_list(strings):
    return all(isinstance(s, str) for s in strings)

def find_longest_string(strings):
    if not is_valid_string_list(strings):
        raise ValueError("All elements must be strings")
    
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))