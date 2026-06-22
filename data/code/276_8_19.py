def repeat_chars(text, U):
    if not isinstance(text, str) or not isinstance(U, int):
        raise ValueError("Invalid input: text must be a string and U must be an integer")
    return ''.join([char * U for char in text])

if __name__ == '__main__':
    sample_text = "Hello World"
    repeat_count = 3
    result = repeat_chars(sample_text, repeat_count)
    print(result)