def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_input = "Python programming is fun and efficient."
    words_list = split_sentence(sample_input)
    print(words_list)