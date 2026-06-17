def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample = "Hello world! This is an efficient Python script."
    result = split_sentence(sample)
    print("Original:", sample)
    print("Words:   ", result)