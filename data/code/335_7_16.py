def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample = "Hello world this is a test case"
    result = split_sentence(sample)
    print(result)