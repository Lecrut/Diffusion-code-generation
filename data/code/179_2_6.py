def reverse_words(sentence: str) -> str:
    return ' '.join(word[::-1] for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    print(reverse_words(sample_sentence))