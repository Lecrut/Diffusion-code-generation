def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    test_string = "Hello world this is a sample"
    result = split_sentence(test_string)
    print(result)