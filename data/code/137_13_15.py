vowels = {'a', 'e', 'i', 'o', 'u'}

def is_vowel(char):
    return char.lower() in vowels
if __name__ == '__main__':
    print(is_vowel('a'))
    print(is_vowel('E'))
    print(is_vowel('z'))