def split_and_clean(text):
    if not text:
        return []
    result = []
    for item in text.split(','):
        cleaned = item.strip()
        if cleaned:
            result.append(cleaned)
    return result

if __name__ == '__main__':
    sample_input = "  apple , banana , , cherry ,  , date "
    print(split_and_clean(sample_input))