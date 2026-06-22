def filter_long_strings(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    
    return [s for s in strings if len(s) <= 5]

if __name__ == '__main__':
    sample_data = ["apple", "cat", "elephant", "dog", "bird"]
    filtered_strings = filter_long_strings(sample_data)
    print(filtered_strings)