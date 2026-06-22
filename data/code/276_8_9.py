CHAR_REPEAT_COUNT = 3

def repeat_characters(text):
    return ''.join([char * CHAR_REPEAT_COUNT for char in text])

if __name__ == '__main__':
    sample_text = "Hello World"
    repeated_text = repeat_characters(sample_text)
    print(repeated_text)