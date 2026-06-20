VALID_INPUT_TYPE = str

def _validate_input(text):
    if not isinstance(text, VALID_INPUT_TYPE):
        raise TypeError("Input must be a string")
    return True

def reverse_word_order(text):
    _validate_input(text)
    words = text.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample_string = "Python is great for coding"
    output = reverse_word_order(sample_string)
    print(output)