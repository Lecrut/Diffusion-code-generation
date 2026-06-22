def filter_and_join_numeric_chars(text):
    return "".join([char for char in text if char.isdigit()])

if __name__ == '__main__':
    sample_text = "abc123def456ghi789"
    result = filter_and_join_numeric_chars(sample_text)
    print(result)