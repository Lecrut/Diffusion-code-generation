def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample = "Hello world, this is an example of Pythonic code."
    result = split_sentence(sample)
    print(result)