def remove_vowels(s):
    vowels = set('aeiouAEIOU')
    return ''.join([c for c in s if c not in vowels])

if __name__ == '__main__':
    print(remove_vowels("Hello World"))
    print(remove_vowels("Python Programming"))
    print(remove_vowels("AEIOUaeiou"))
    print(remove_vowels(""))
    print(remove_vowels("bcdfg"))