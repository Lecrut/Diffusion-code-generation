def split_string(input_string):
    return list(input_string)

if __name__ == '__main__':
    sample_strings = {
        "hello": None,
        "world": None,
        "Python": None
    }
    
    for sample, _ in sample_strings.items():
        result = split_string(sample)
        print(f"Input: {sample}, Output: {result}")