vowels = set('aeiouAEIOU')

def is_vowel(char):
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError('Input must be a single character')
    return char in vowels
if __name__ == '__main__':
    print(is_vowel('a'))
    print(is_vowel('b'))
    print(is_vowel('E'))
    print(is_vowel('z'))