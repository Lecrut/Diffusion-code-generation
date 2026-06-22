def reverse_words(input_string):
    if not isinstance(input_string, str) or not input_string.strip():
        raise ValueError('Input must be a non-empty string')
    words = input_string.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
if __name__ == '__main__':
    sample_input = 'Hello world from Python'
    result = reverse_words(sample_input)
    print(result)