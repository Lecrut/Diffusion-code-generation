import string

def find_frequency_duplicates(text: str) -> list[tuple[str, int]]:
    frequencies = {}
    for char in text:
        if char in string.whitespace or char in string.punctuation:
            continue
        if char.isalpha():
            lower_char = char.lower()
            frequencies[lower_char] = frequencies.get(lower_char, 0) + 1

    duplicates = []
    for char, count in frequencies.items():
        if count > 1:
            duplicates.append((char, count))

    duplicates.sort(key=lambda item: (-item[1], item[0]))
    return duplicates

if __name__ == '__main__':
    sample_text = "Astronomers saw a starry sky near the moon. The light was dim."
    result = find_frequency_duplicates(sample_text)
    print(result)