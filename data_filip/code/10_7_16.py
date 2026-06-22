def reverse_words(sentence: str) -> str:
    words = sentence.split()
    result = []
    index = len(words) - 1
    while index >= 0:
        result.append(words[index])
        index -= 1
    return ' '.join(result)

if __name__ == '__main__':
    sample_input = "The quick brown fox jumps over the lazy dog"
    print(reverse_words(sample_input))