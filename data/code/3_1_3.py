import string
VOWELS = set('aeiouAEIOU')
ALL_CHARS = ''.join((chr(i) for i in range(256)))
VOWEL_TABLE = str.maketrans('', '', string.ascii_lowercase + string.ascii_uppercase)
_VOWEL_TO_NONE = {ord(c): None for c in 'aeiouAEIOU'}

def strip_vowels(text):
    return text.translate(_VOWEL_TO_NONE)
if __name__ == '__main__':
    sample_text = 'Hello World!'
    result = strip_vowels(sample_text)
    print(result)