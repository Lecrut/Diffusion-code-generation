def reverse_words(input_string):
    words = input_string.split()
    reversed_words = [word for word in reversed(words) if word]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_input = "   Hello   world!  "
    print(reverse_words(sample_input))