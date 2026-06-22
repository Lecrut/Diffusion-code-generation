def reverse_word_order(input_string):
    words = input_string.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    result = reverse_word_order(sample_text)
    print(result)