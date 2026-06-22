import string

VOWELS = set('aeiouAEIOU')
VOWEL_BYTES = [ord(c) for c in VOWELS]
TRANS_TABLE = bytes([0 if i in VOWEL_BYTES else i for i in range(256)])

def strip_vowels(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.translate(TRANS_TABLE)

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = strip_vowels(sample_text)
    print(result)