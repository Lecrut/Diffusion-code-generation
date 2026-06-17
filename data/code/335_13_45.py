def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_text = "Hello world, this is an example of splitting sentences efficiently."
    result_words = split_sentence(sample_text)
    print("Original Sentence:", sample_text)
    print("Split Words: ", result_words)