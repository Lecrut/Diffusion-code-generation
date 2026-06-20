def remove_vowels(s):
    return ''.join([c for c in s if c.lower() not in 'aeiou'])

if __name__ == '__main__':
    print(remove_vowels('Hello World'))
    print(remove_vowels('Python'))
    print(remove_vowels('AEIOU'))
    print(remove_vowels('aeiou'))
    print(remove_vowels(''))
    print(remove_vowels('bcdfg'))
    print(remove_vowels('aEiOu'))