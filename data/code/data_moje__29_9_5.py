import string

TRANSLATION_TABLE = str.maketrans('', '', ''.join(c for c in string.ascii_lowercase if c not in 'aeiouAEIOU'))

def count_vowels(text):
    cleaned_text = text.translate(TRANSLATION_TABLE)
    return len(cleaned_text)

if __name__ == '__main__':
    large_string = "This is a very large string with many vowels like a e i o u and sometimes y, but y is tricky so we ignore it here. We repeat this pattern many many times to make the string huge. A e i o u A E I O U." * 10000
    result = count_vowels(large_string)
    print(result)