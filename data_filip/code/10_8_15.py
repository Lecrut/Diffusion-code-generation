def reverse_words(sentence: str) -> str:
    if not sentence:
        return ""
    words = sentence.split()
    if not words:
        return ""
    reversed_words = words[::-1]
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "the quick brown fox jumps over the lazy dog"
    result = reverse_words(sample_sentence)
    print(result)