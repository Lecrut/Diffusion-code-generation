import string

VOWELS = set("aeiouAEIOU")

_TRANSLATION_TABLE = str.maketrans({k: "" for k in VOWELS})

def strip_vowels(text: str) -> str:
    return text.translate(_TRANSLATION_TABLE)

if __name__ == '__main__':
    result = strip_vowels("Hello World!")
    print(result)