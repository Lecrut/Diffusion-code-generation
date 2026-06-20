vowels = set('aeiouAEIOU')

def is_vowel(char):
    return char in vowels
if __name__ == '__main__':
    print(is_vowel('a'))
    print(is_vowel('A'))
    print(is_vowel('b'))
    print(is_vowel('E'))