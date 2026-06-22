def split_and_clean_string(text):
    result = []
    for segment in text.split(','):
        cleaned = segment.strip()
        if cleaned:
            result.append(cleaned)
    return result

if __name__ == '__main__':
    sample_text = "  apple , banana,  , orange , ,  grape  "
    print(split_and_clean_string(sample_text))