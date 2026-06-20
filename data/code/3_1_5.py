import string

VOWELS = 'aeiouAEIOU'
TABLE = str.maketrans('', '', VOWELS)

def strip_vowels(text: str) -> str:
    return text.translate(TABLE)

if __name__ == '__main__':
    sample_text = 'Hello World'
    result = strip_vowels(sample_text)
    print(result)