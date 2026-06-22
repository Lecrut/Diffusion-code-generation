def remove_vowels(s):
    return ''.join(filter(lambda c: c.lower() not in 'aeiou', s))

if __name__ == '__main__':
    print(remove_vowels("Hello World"))
    print(remove_vowels("Python Programming"))
    print(remove_vowels("AEIOU aeiou"))
    print(remove_vowels("bcdfg"))
    print(remove_vowels(""))