def split_and_filter(text):
    if not text:
        return []
    segments = text.split(',')
    result = []
    for segment in segments:
        stripped = segment.strip()
        if stripped:
            result.append(stripped)
    return result

if __name__ == '__main__':
    sample_text = "  apple , banana,, ,cherry , , date "
    print(split_and_filter(sample_text))
    empty_text = ",,,  ,  "
    print(split_and_filter(empty_text))
    mixed_text = "red, green,  ,blue, ,yellow"
    print(split_and_filter(mixed_text))