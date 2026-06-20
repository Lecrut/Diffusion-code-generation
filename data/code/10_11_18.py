def reverse_words(sentence: str) -> str:
    words = sentence.split()
    return ' '.join(reversed(words))

if __name__ == '__main__':
    sample = "  hello   world  "
    print(reverse_words(sample))
    sample2 = "Python is great"
    print(reverse_words(sample2))
    sample3 = "   "
    print(reverse_words(sample3))
    sample4 = "single"
    print(reverse_words(sample4))