def contains_vowel(s: str) -> bool:
    vowels = set('aeiouAEIOU')
    return any(char in vowels for char in s)

if __name__ == '__main__':
    test_strings = ["hello", "rhythm", "AEIOU", "", "bcdf"]
    results = {s: contains_vowel(s) for s in test_strings}
    for string, has_vowel in results.items():
        print(f"'{string}' contains a vowel: {has_vowel}")