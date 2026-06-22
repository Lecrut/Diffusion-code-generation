def validate_input(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    if len(word) == 0:
        raise ValueError("Input cannot be an empty string")

def reverse_word(word):
    validate_input(word)
    return word[::-1]

if __name__ == '__main__':
    sample_word = "hello"
    try:
        reversed_word = reverse_word(sample_word)
        print(reversed_word)
    except ValueError as e:
        print(e)