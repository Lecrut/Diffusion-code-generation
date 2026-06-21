def reverse_words(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    print(reverse_words(sample_sentence))