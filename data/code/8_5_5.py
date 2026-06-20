def split_and_strip(text):
    return [part.strip() for part in text.split(',')]

if __name__ == '__main__':
    sample_text = "  apple , banana ,  cherry  , date"
    result = split_and_strip(sample_text)
    print(result)