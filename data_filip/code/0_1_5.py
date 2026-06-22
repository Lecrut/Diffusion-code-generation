def filter_and_join_numeric_chars(text):
    return "".join([char for char in text if char.isnumeric()])

if __name__ == '__main__':
    sample_text = "abc123!@#456"
    result = filter_and_join_numeric_chars(sample_text)
    print(result)