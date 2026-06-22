def is_alphabetic(string):
    return string.isalpha()

def filter_alphabetic_strings(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings")
    
    return [s for s in strings if is_alphabetic(s)]

if __name__ == '__main__':
    sample_values = ["hello", "world", "123", "test", "!@#"]
    result = filter_alphabetic_strings(sample_values)
    print(result)