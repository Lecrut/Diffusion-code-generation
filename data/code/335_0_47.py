def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_string = "Hello world Python programming"
    result = split_words(sample_string)
    print(result)