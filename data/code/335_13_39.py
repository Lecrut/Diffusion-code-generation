def split_sentence_efficiently(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Python is great, isn't it?  It's a fantastic language."
    words_list = split_sentence_efficiently(sample_sentence)
    assert isinstance(words_list, list), "Output must be a list"
    print(f"Input: {sample_sentence}")
    print(f"Parsed Words ({len(words_list)} total):")
    for i, word in enumerate(words_list, 1):
        print(f"Word {i}: '{word}'")