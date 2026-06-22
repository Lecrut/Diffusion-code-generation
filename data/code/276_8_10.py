def repeat_chars(text, n):
    return ''.join([char * n for char in text])

if __name__ == '__main__':
    original_text = "Python"
    repetition_count = 3
    result = repeat_chars(original_text, repetition_count)
    print(result)