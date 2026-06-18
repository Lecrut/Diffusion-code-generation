def split_into_words(text: str) -> list[str]:
    return [word for word in text.split() if word]
if __name__ == '__main__':
    sample_input = "Hello, World! This is Python."
    result = split_into_words(sample_input)
    print(result)