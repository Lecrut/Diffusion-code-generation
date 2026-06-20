VOWELS = set('aeiou')

def is_vowel(char):
    return char.lower() in VOWELS
if __name__ == '__main__':
    print(is_vowel('a'))
    print(is_vowel('E'))
    print(is_vowel('z'))
    print(is_vowel('i'))