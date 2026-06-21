def find_duplicate_characters(text):
    if not text:
        return []
    counts = {}
    for char in text:
        if char.isalpha():
            key = char.lower()
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1
    result = []
    for char, count in counts.items():
        if count > 1:
            result.append(char)
    return sorted(result)

if __name__ == '__main__':
    sample_string = "Programming is fun"
    duplicates = find_duplicate_characters(sample_string)
    print(duplicates)