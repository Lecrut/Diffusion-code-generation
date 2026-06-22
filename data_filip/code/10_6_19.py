def reverse_word_order(text):
    words = text.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "the quick brown fox",
        "single"
    ]

    for s in sample_strings:
        print(reverse_word_order(s))