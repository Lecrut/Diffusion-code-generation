def count_vowels(s):
    return sum(1 for c in s if c.lower() in 'aeiou')

if __name__ == '__main__':
    print(count_vowels('hello'))
    print(count_vowels('world'))
    print(count_vowels('aeiou'))
    print(count_vowels('bcdfg'))
    print(count_vowels('AEIOU'))
    print(count_vowels(''))