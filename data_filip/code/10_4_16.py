def reverse_word_order(text):
    words = text.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_input = "Hello world this is a test"
    result = reverse_word_order(sample_input)
    print(result)