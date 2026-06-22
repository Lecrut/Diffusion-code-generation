def find_min_lexicographical(strings):
    if not strings:
        raise ValueError("The list is empty")
    
    min_string = strings[0]
    for string in strings[1:]:
        if string < min_string:
            min_string = string
    
    return min_string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_min_lexicographical(sample_strings))