def reverse_words(input_string):
    words = input_string.split()
    reversed_words = list(reversed(words))
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_input = "Python is fun"
    result = reverse_words(sample_input)
    print(result)