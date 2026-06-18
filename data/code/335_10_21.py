def split_sentence(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_input = "Hello world Python programming is fun"
    result = split_sentence(sample_input)
    print(result)