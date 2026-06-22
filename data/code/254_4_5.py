def min_by_length(strings):
    if not strings:
        raise ValueError("The list cannot be empty")
    
    min_string = strings[0]
    for string in strings:
        if len(string) < len(min_string):
            min_string = string
    
    return min_string

if __name__ == '__main__':
    sample_values = ["hello", "world", "this", "is", "a", "test"]
    print(min_by_length(sample_values))