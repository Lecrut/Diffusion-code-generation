import string

VOWELS = set('aeiouAEIOU')
_VOWEL_CODES = [ord(c) for c in string.printable if c in VOWELS]
_VOWEL_REPLACEMENT = [None] * 128
for code in _VOWEL_CODES:
    _VOWEL_REPLACEMENT[code] = None

def strip_vowels(text: str) -> str:
    return text.translate(_VOWEL_REPLACEMENT)

if __name__ == '__main__':
    sample_text = "Hello World 123!"
    result = strip_vowels(sample_text)
    print(result)