def remove_vowels(s):
    trans_table = str.maketrans('', '', 'aeiouAEIOU')
    return s.translate(trans_table)

if __name__ == '__main__':
    sample = "Hello World"
    print(remove_vowels(sample))
    sample2 = "AEIOUaeiou"
    print(remove_vowels(sample2))
    sample3 = "Python Programming"
    print(remove_vowels(sample3))