def split_and_strip(text):
    if not text:
        return []
    parts = text.split(',')
    return [part.strip() for part in parts]

if __name__ == '__main__':
    sample_text = "  apple  , banana , cherry  ,  date "
    result = split_and_strip(sample_text)
    print(result)