def detect_frequency_duplicates(text):
    if not text:
        return []
    frequency_map = {}
    for char in text:
        frequency_map[char] = frequency_map.get(char, 0) + 1
    count_map = {}
    for count in frequency_map.values():
        count_map[count] = count_map.get(count, 0) + 1
    duplicates = []
    for char, count in frequency_map.items():
        if count_map[count] > 1:
            duplicates.append((char, count))
    duplicates.sort(key=lambda x: (-x[1], x[0]))
    return duplicates

if __name__ == '__main__':
    sample_text = "hello world programming"
    result = detect_frequency_duplicates(sample_text)
    print(result)