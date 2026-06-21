def reverse_words(sentence: str) -> str:
    return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(reverse_words(sample_sentence))