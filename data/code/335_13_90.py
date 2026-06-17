def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample = "Hello world! This is a test."
    result = split_sentence(sample)
    print(result)