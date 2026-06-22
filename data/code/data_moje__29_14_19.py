def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

if __name__ == '__main__':
    print(count_vowels('hello'))
    print(count_vowels('world'))
    print(count_vowels('Python Programming'))
    print(count_vowels('AEIOU'))
    print(count_vowels('xyz'))
    print(count_vowels(''))