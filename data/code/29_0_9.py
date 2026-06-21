VOWEL_MAP = {
    'a': 1,
    'e': 1,
    'i': 1,
    'o': 1,
    'u': 1,
    'A': 1,
    'E': 1,
    'I': 1,
    'O': 1,
    'U': 1
}

def count_vowels(s):
    total = 0
    lookup = VOWEL_MAP
    for char in s:
        if char in lookup:
            total += 1
    return total

if __name__ == '__main__':
    test_inputs = [
        "The Quick Brown Fox",
        "AI and ML are transforming the world",
        "xyz",
        "aeiou",
        "Rhythm",
        "Education"
    ]
    for text in test_inputs:
        print(count_vowels(text))