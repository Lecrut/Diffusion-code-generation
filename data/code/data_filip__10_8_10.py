def reverse_words(sentence: str) -> str:
    words = sentence.split()
    return ' '.join(reversed(words))

if __name__ == '__main__':
    result = reverse_words("the sky is blue")
    print(result)