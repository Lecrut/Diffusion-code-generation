import collections

def detect_character_duplicates(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    frequency_map = collections.Counter(text)
    duplicates = {char: count for char, count in frequency_map.items() if count > 1}
    return duplicates

if __name__ == '__main__':
    sample_text = "programming"
    result = detect_character_duplicates(sample_text)
    print(result)