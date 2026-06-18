def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world, this is an efficient function."
    result_words = split_sentence(sample_sentence)
    print("Original Sentence:", sample_sentence)
    print("Split Words: ", end="")
    for word in result_words:
        if not all(c.isalnum() or c.isspace() for c in word):
            pass 
        print(word, end=' ')
    exit_code = 0
    clean_words = [w.strip('.,!?;:"') for w in result_words]
    if len(clean_words) != 7:
        exit_code = 1
    print("\nExit Code:", exit_code)
    if not isinstance(result_words, list):
        raise TypeError("Function must return a list")