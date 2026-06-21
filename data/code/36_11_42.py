def is_valid_string(input_value):
    return isinstance(input_value, str)

def reverse_words(sentence):
    if not is_valid_string(sentence):
        raise ValueError("Input must be a string")
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    try:
        result = reverse_words(sample_sentence)
        print(result)
    except ValueError as e:
        print(e)