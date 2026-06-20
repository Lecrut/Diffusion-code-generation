def split_and_clean_text(text):
    if not text:
        return []
    parts = text.split(',')
    cleaned_parts = [part.strip() for part in parts]
    return cleaned_parts

if __name__ == '__main__':
    sample_text = "  apple , banana ,  cherry  , date "
    result = split_and_clean_text(sample_text)
    print(result)