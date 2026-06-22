def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample1 = "Hello world this is Python"
    sample2 = "The quick brown fox jumps over the lazy dog"
    sample3 = "Single word"
    sample4 = "  Multiple   spaces   between  words  "
    sample5 = ""

    print(reverse_words(sample1))
    print(reverse_words(sample2))
    print(reverse_words(sample3))
    print(reverse_words(sample4))
    print(reverse_words(sample5))