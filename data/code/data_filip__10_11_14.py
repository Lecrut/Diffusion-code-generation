def reverse_words_in_sentence(sentence: str) -> str:
    words = sentence.split()
    words.reverse()
    result = ' '.join(words)
    return result

if __name__ == '__main__':
    sample = "  Hello   world!  This is  a test.  "
    res = reverse_words_in_sentence(sample)
    print(res)