def split_sentence(text: str) -> list[str]:
    return [word for word in text.split()]
if __name__ == '__main__':
    sample_input = "Hello world this is a test"
    result = split_sentence(sample_input)
    print(result)