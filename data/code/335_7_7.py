def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample = "This is a test of the function."
    result = split_sentence(sample)
    print(result)