def remove_vowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    return ''.join(c for c in s if c not in vowels)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Python Programming"
    sample3 = "AEIOUaeiou"
    sample4 = "No Vowels Here: Rhythm"

    print(remove_vowels(sample1))
    print(remove_vowels(sample2))
    print(remove_vowels(sample3))
    print(remove_vowels(sample4))