def find_duplicate_frequencies(text):
    if not text:
        return []

    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    freq_map = {}
    for char, count in char_counts.items():
        if count in freq_map:
            freq_map[count].append(char)
        else:
            freq_map[count] = [char]

    duplicates = []
    for count, chars in freq_map.items():
        if len(chars) > 1:
            duplicates.append((count, sorted(chars)))

    return sorted(duplicates, key=lambda x: x[0])

if __name__ == '__main__':
    sample_text = "mississippi"
    result = find_duplicate_frequencies(sample_text)
    print(result)