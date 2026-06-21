def reverse_words(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
if __name__ == '__main__':
    sample_input = '  The   quick brown fox jumps over the lazy dog  '
    result = reverse_words(sample_input)
    print(result)