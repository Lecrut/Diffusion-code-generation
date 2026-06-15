def contains_vowel(s: str) -> bool:
    for char in s:
        if char in 'aeiouAEIOU':
            return True
    return False
if __name__ == '__main__':
    print(contains_vowel("hello"))
    print(contains_vowel("rhythm"))
    print(contains_vowel("AEIOU"))
    print(contains_vowel(""))
    print(contains_vowel("bcdf"))