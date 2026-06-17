def split_sentence(sentence: str) -> list[str]:
    return [word for word in sentence.split()]
if __name__ == '__main__':
    sample_input = "Hello world this is Python"
    result_words = split_sentence(sample_input)
    print(result_words)