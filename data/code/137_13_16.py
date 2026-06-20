class VowelChecker:
    VOWELS = set('aeiou')

    @staticmethod
    def is_vowel(char):
        return char.lower() in VowelChecker.VOWELS
if __name__ == '__main__':
    print(VowelChecker.is_vowel('a'))
    print(VowelChecker.is_vowel('E'))
    print(VowelChecker.is_vowel('z'))