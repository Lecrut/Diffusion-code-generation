def remove_vowels(s):
    return ''.join([c for c in s if c.lower() not in 'aeiou'])

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Python Programming"
    sample3 = "AEIOU aeiou"
    print(remove_vowels(sample1))
    print(remove_vowels(sample2))
    print(remove_vowels(sample3))