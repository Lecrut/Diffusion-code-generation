def split_and_normalize(text):
    parts = text.split(',')
    normalized = [part.strip().lower() for part in parts if part.strip()]
    seen = set()
    unique = []
    for item in normalized:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique

if __name__ == '__main__':
    sample_string = "Apple, banana, APPLE, Banana, cherry, Banana, date, CHERRY"
    result = split_and_normalize(sample_string)
    print(result)