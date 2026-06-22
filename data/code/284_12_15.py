def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def split_and_reverse(words):
    return words[::-1]

def reverse_words(input_string):
    validate_input(input_string)
    words = input_string.split()
    reversed_words = split_and_reverse(words)
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_input = "Hello world from Python"
    result = reverse_words(sample_input)
    print(result)