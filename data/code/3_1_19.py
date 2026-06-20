import string

VOWELS = set('aeiouAEIOU')
TRANS_TABLE = str.maketrans({v: None for v in VOWELS})

def strip_vowels(text: str) -> str:
    return text.translate(TRANS_TABLE)

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = strip_vowels(sample_text)
    print(result)