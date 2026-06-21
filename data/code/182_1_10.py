def split_string(input_string):
    return list(input_string)

if __name__ == '__main__':
    sample_strings = {
        "hello": ["h", "e", "l", "l", "o"],
        "world": ["w", "o", "r", "l", "d"],
        "Python": ["P", "y", "t", "h", "o", "n"]
    }
    
    for sample_string, expected_result in sample_strings.items():
        result = split_string(sample_string)
        print(f"Input: {sample_string}, Output: {result}")