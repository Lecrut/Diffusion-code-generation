import string

TRANSLATE_TABLE = str.maketrans('', '', ''.join(set(string.ascii_letters) - set('aeiouAEIOU')))

def count_vowels(text: str) -> int:
    return len(text.translate(TRANSLATE_TABLE))

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog in a field of green grass where the sun shines bright and the birds sing loud songs of joy."
    result = count_vowels(sample_text)
    print(result)