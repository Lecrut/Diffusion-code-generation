def has_unique_characters(input_str):
    return len(input_str) == len(set(input_str))

if __name__ == '__main__':
    sample_strings = ['abcdefg', 'hello', 'world', 'Python']
    for sample in sample_strings:
        result = has_unique_characters(sample)
        print(result)