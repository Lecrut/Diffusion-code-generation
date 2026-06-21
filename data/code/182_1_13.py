def split_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    return list(input_string)

if __name__ == '__main__':
    sample_strings = ["hello", "world", "Python"]
    for sample_string in sample_strings:
        result = split_string(sample_string)
        print(f"Input: {sample_string}, Output: {result}")