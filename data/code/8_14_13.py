def split_and_normalize(s):
    parts = s.split(',')
    normalized = [p.strip().lower() for p in parts]
    seen = set()
    result = []
    for item in normalized:
        if item and item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample = "apple, Banana, APPLE, cherry, banana,  date "
    output = split_and_normalize(sample)
    print(output)