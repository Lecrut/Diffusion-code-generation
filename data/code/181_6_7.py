VOWELS = set('aeiouAEIOU')

def contains_vowel(s: str) -> bool:
    return any(char in VOWELS for char in s)

if __name__ == '__main__':
    test_strings = ["hello", "rhythm", "aeiou", "", "Bcdfghjkl"]
    results = {s: contains_vowel(s) for s in test_strings}
    for string, result in results.items():
        print(f"'{string}' contains a vowel: {result}")