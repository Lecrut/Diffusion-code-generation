def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample = "Hello world Python programming is fun"
    result = split_sentence(sample)
    print(result)