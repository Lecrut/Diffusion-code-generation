VOWELS = set('aeiouAEIOU')

def is_vowel(char):
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError('Input must be a single character.')
    return char in VOWELS
if __name__ == '__main__':
    print(is_vowel('a'))
    print(is_vowel('e'))
    print(is_vowel('i'))
    print(is_vowel('o'))
    print(is_vowel('u'))
    print(is_vowel('A'))
    print(is_vowel('E'))
    print(is_vowel('I'))
    print(is_vowel('O'))
    print(is_vowel('U'))
    print(is_vowel('b'))
    try:
        print(is_vowel('ab'))
    except ValueError as e:
        print(e)