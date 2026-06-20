class VowelChecker:

    def __init__(self):
        self.vowels = {'a', 'e', 'i', 'o', 'u'}

    def is_vowel(self, char):
        return char.lower() in self.vowels
if __name__ == '__main__':
    checker = VowelChecker()
    print(checker.is_vowel('A'))
    print(checker.is_vowel('b'))
    print(checker.is_vowel('E'))
    print(checker.is_vowel('z'))