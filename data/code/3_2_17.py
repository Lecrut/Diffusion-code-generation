import re

VOWEL_MAP = {
    'a': 'vowel', 'e': 'vowel', 'i': 'vowel', 'o': 'vowel', 'u': 'vowel',
    'A': 'vowel', 'E': 'vowel', 'I': 'vowel', 'O': 'vowel', 'U': 'vowel'
}

def strip_vowels(input_text):
    char_list = []
    for char in input_text:
        if VOWEL_MAP.get(char) != 'vowel':
            char_list.append(char)
    return "".join(char_list)

if __name__ == '__main__':
    raw_input = "Programming is awesome!"
    cleaned = strip_vowels(raw_input)
    print(cleaned)