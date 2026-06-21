def split_string(input_string):
    return list(input_string)

if __name__ == '__main__':
    sample_strings = ["hello", "world", "Python"]
    for string in sample_strings:
        result = split_string(string)
        print(f"Input: {string}, Output: {result}")