import string

VOWELS = set('aeiouAEIOU')
TRANSLATE_TABLE = str.maketrans('', '', string.ascii_letters.translate(str.maketrans('', '', ''.join(VOWELS))))

def strip_vowels(text: str) -> str:
    return text.translate(TRANSLATE_TABLE)

if __name__ == '__main__':
    result = strip_vowels("Hello World")
    print(result)