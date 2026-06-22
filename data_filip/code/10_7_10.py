def reverse_words(sentence: str) -> str:
    words = sentence.split()
    result = []
    i = len(words) - 1
    while i >= 0:
        result.append(words[i])
        i -= 1
    return ' '.join(result)

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    reversed_sentence = reverse_words(sample_sentence)
    print(reversed_sentence)