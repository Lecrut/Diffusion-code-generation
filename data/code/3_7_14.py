VOWEL_MAP = {
    'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
    'A': True, 'E': True, 'I': True, 'O': True, 'U': True
}

def remove_vowels(text: str) -> str:
    return ''.join(char for char in text if not VOWEL_MAP.get(char, False))

if __name__ == '__main__':
    test_phrase = "The quick brown fox jumps over the lazy dog"
    output = remove_vowels(test_phrase)
    print(output)