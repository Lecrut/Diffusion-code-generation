def reverse_words(sentence: str) -> str:
    return ' '.join(reversed(sentence.split()))

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    print(reverse_words(sample_text))