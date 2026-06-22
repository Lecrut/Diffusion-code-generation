def repeat_chars(text, U):
    return ''.join([char * U for char in text])

if __name__ == '__main__':
    sample_text = "abc"
    multiplier = 3
    repeated_text = repeat_chars(sample_text, multiplier)
    print(repeated_text)