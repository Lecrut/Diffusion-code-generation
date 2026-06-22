def split_and_strip_text(text):
    parts = text.split(',')
    return [part.strip() for part in parts]

if __name__ == '__main__':
    sample_text = "  apple , banana  ,  orange  , grape  "
    result = split_and_strip_text(sample_text)
    print(result)