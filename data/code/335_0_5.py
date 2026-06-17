def split_string_into_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_input = "Hello world Python programming"
    result = split_string_into_words(sample_input)
    print(result)