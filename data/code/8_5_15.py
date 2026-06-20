def split_and_trim(text):
    return [part.strip() for part in text.split(',')]

if __name__ == '__main__':
    sample_text = " apple,  banana,cherry , date"
    result = split_and_trim(sample_text)
    print(result)