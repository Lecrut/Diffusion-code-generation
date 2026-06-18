def split_sentence(sentence: str) -> list[str]:
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string.")
    return sentence.split()
if __name__ == '__main__':
    sample_input = "Hello world Python programming"
    result = split_sentence(sample_input)
    print(result)