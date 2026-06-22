def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentences = [
        "Hello World",
        "  Hello   World  ",
        "The  quick  brown  fox",
        "Single",
        "",
        "   "
    ]
    for sentence in sample_sentences:
        result = reverse_words(sentence)
        print(result)