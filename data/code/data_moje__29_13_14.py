VOWEL_MAP = {
    'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
    'A': True, 'E': True, 'I': True, 'O': True, 'U': True
}

def count_vowels(text: str) -> int:
    total = 0
    for char in text:
        if VOWEL_MAP.get(char, False):
            total += 1
    return total

if __name__ == '__main__':
    static_text = "Python programming is fun"
    print(count_vowels(static_text))