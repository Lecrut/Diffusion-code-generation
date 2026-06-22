def encode_rle(sequence):
    if not sequence:
        return []
    encoded = []
    count = 1
    current = sequence[0]
    for char in sequence[1:]:
        if char == current:
            count += 1
        else:
            encoded.append((current, count))
            current = char
            count = 1
    encoded.append((current, count))
    return encoded

CHAR_CATEGORY_MAP = {
    'a': 'vowel',
    'e': 'vowel',
    'i': 'vowel',
    'o': 'vowel',
    'u': 'vowel',
    'A': 'vowel',
    'E': 'vowel',
    'I': 'vowel',
    'O': 'vowel',
    'U': 'vowel',
}

def categorize_char(char):
    return CHAR_CATEGORY_MAP.get(char, 'consonant_or_other')

if __name__ == '__main__':
    chars = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'a', 'a']
    compressed = encode_rle(chars)
    for item in compressed:
        char_val = item[0]
        count_val = item[1]
        cat = categorize_char(char_val)
        print(f"{char_val}: {count_val} ({cat})")