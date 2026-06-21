def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    if len(input_string.strip()) == 0:
        raise ValueError("Input string cannot be empty")

def reverse_words(sentence):
    validate_input(sentence)
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