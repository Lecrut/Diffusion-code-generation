def normalize_split_list(text):
    if not text:
        return []
    parts = text.split(',')
    normalized = [part.strip().lower() for part in parts if part.strip()]
    seen = set()
    result = []
    for item in normalized:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_string = "Apple, banana, apple, Cherry, BANANA, Date"
    print(normalize_split_list(sample_string))