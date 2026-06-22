def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_text = "the quick brown fox jumps over the lazy dog"
    result = reverse_words(sample_text)
    print(result)