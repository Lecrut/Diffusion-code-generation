def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    result = split_words(sample_input)
    print(result)