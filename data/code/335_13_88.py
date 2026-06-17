def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_text = "Hello world, this is an efficient Python function."
    result = split_sentence(sample_text)
    print(result)