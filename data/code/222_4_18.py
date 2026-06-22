def find_min_lexicographical(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings")
    
    min_str = strings[0]
    for string in strings[1:]:
        if string < min_str:
            min_str = string
    
    return min_str

if __name__ == '__main__':
    sample_values = ["zebra", "apple", "cherry", "banana"]
    result = find_min_lexicographical(sample_values)
    print(f"Minimum lexicographical value: {result}")