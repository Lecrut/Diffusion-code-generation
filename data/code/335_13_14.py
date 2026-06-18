def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world, this is an example of Pythonic code."
    result_words = split_sentence(sample_sentence)
    print("Original Sentence:", sample_sentence)
    print("Split Words: ", end="")
    for word in result_words:
        if len(word.strip()) > 0:
            print(f"'{word}'", end=' ')