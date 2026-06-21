def detect_duplicate_frequencies(text):
    frequency_map = {}
    for char in text:
        frequency_map[char] = frequency_map.get(char, 0) + 1

    frequency_reverse = {}
    duplicates = []
    for char, freq in frequency_map.items():
        if freq in frequency_reverse:
            duplicates.append(char)
        else:
            frequency_reverse[freq] = char

    return duplicates

if __name__ == '__main__':
    sample_text = "hello world"
    print(detect_duplicate_frequencies(sample_text))