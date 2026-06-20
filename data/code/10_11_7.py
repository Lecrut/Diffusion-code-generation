def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentences = [
        "Hello World",
        "  Hello   World  ",
        "   ",
        "Python is great",
        "  Multiple   spaces   here  "
    ]
    for sentence in sample_sentences:
        print(reverse_words(sentence))