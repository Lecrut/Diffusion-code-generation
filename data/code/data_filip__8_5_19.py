def split_and_strip(text):
    parts = text.split(',')
    return [part.strip() for part in parts]

if __name__ == '__main__':
    sample_text = " apple , banana , cherry "
    result = split_and_strip(sample_text)
    print(result)