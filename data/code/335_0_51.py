def split_string_to_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_input = "Hello, world! This is a test."
    result = split_string_to_words(sample_input)
    print(result)