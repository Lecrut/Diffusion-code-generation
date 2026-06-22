def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "the quick brown fox jumps over the lazy dog"
    sample3 = "Python is awesome"
    print(reverse_words(sample1))
    print(reverse_words(sample2))
    print(reverse_words(sample3))