def split_and_normalize(text):
    parts = text.split(',')
    normalized = [part.strip().lower() for part in parts]
    seen = set()
    result = []
    for item in normalized:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample = "Apple, banana, Apple, Banana, cherry, CHERRY, date, Date"
    output = split_and_normalize(sample)
    print(output)