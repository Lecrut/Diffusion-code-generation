def print_characters_from_string(s, indices):
    if not isinstance(s, str) or not all(isinstance(i, int) for i in indices):
        raise ValueError("Invalid input types")
    
    for index in indices:
        if 0 <= index < len(s):
            print(s[index])
        else:
            print(f"Index {index} out of range")

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [0, 7, 12, 5, 10]
    print_characters_from_string(sample_string, sample_indices)