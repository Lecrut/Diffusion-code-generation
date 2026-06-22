def repeat_chars(text, u):
    return ''.join([char * u for char in text])

if __name__ == '__main__':
    sample_text = "Hello World"
    multiplier = 3
    result = repeat_chars(sample_text, multiplier)
    print(result)