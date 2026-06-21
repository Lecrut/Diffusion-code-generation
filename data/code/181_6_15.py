class VowelChecker:
    def __init__(self):
        self.vowels = set('aeiouAEIOU')

    def contains_vowel(self, s: str) -> bool:
        return any(char in self.vowels for char in s)

if __name__ == '__main__':
    checker = VowelChecker()
    test_strings = ["hello", "rhythm", "aeiou", "", "Bcdfghjkl"]
    results = {s: checker.contains_vowel(s) for s in test_strings}
    print(results)