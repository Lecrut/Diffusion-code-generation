def split_sentence(sentence: str) -> list[str]:
    return [word for word in sentence.strip().split()]
if __name__ == '__main__':
    sample_sentence = "Hello, World! This is an efficient Python script."
    result_words = split_sentence(sample_sentence)
    print("Words:", result_words)