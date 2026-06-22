def reverse_word_order(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    result = reverse_word_order(sample_text)
    print(result)