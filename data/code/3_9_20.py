VOWEL_REMOVE = str.maketrans('', '', 'aeiouAEIOU')

def remove_vowels(s):
    return s.translate(VOWEL_REMOVE)

if __name__ == '__main__':
    sample = "Hello World"
    print(remove_vowels(sample))
    sample2 = "Python Programming"
    print(remove_vowels(sample2))
    sample3 = "AEIOU aeiou"
    print(remove_vowels(sample3))