def remove_vowels(s):
    vowels = set('aeiouAEIOU')
    return ''.join([c for c in s if c not in vowels])

if __name__ == '__main__':
    print(remove_vowels("Hello World"))
    print(remove_vowels("Python Programming"))
    print(remove_vowels("AEIOU aeiou"))
    print(remove_vowels("No Vowels Here"))
    print(remove_vowels("12345!@#$%"))