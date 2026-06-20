def split_and_strip(text):
    if not text:
        return []
    return [part.strip() for part in text.split(',')]

if __name__ == '__main__':
    sample_input = "  apple  , banana ,  cherry  , date "
    result = split_and_strip(sample_input)
    print(result)