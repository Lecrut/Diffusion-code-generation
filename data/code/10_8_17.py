def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentences = [
        "Hello World",
        "The quick brown fox jumps over the lazy dog",
        "Python is awesome",
        "SingleWord",
        "   Leading and trailing   spaces   ",
        ""
    ]
    for s in sample_sentences:
        print(reverse_words(s))