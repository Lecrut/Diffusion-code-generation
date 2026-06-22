remove_vowels = str.maketrans('', '', 'aeiouAEIOU')

def remove_vowels_from_string(s):
    return s.translate(remove_vowels)

if __name__ == '__main__':
    sample = "Hello World"
    print(remove_vowels_from_string(sample))
    sample2 = "Python Programming"
    print(remove_vowels_from_string(sample2))
    sample3 = "AEIOU aeiou"
    print(remove_vowels_from_string(sample3))