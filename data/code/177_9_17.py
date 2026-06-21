def split_string_by_whitespace(text):
    return text.split()

if __name__ == '__main__':
    sample1 = "data analysis with python"
    result1 = split_string_by_whitespace(sample1)
    print(f"Input: '{sample1}'")
    print(f"Output: {result1}")