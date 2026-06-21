import string

TRANSLATION_TABLE = None

def _init_translation_table():
    global TRANSLATION_TABLE
    all_chars = string.ascii_lowercase + string.ascii_uppercase
    vowels = set('aeiouAEIOU')
    keep = [c if c in vowels else '' for c in all_chars]
    map_list = list(all_chars)
    for i, char in enumerate(all_chars):
        map_list[i] = keep[i]
    TRANSLATION_TABLE = str.maketrans('', '', ''.join(c for c in all_chars if c not in vowels))

def count_vowels(text):
    if TRANSLATION_TABLE is None:
        _init_translation_table()
    remaining_text = text.translate(TRANSLATION_TABLE)
    return len(remaining_text)

if __name__ == '__main__':
    sample_string = "The Quick Brown Fox Jumps Over The Lazy Dog 12345!@#aeiouAEIOU"
    result = count_vowels(sample_string)
    print(result)