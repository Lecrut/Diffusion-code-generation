def repeat_chars(text, U):
    return ''.join([char * U for char in text])
if __name__ == '__main__':
    sample_text = 'abc'
    repetition_count = 3
    result = repeat_chars(sample_text, repetition_count)
    print(result)