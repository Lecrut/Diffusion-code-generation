def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    trans_table = str.maketrans('', '', vowels)
    return s.translate(trans_table)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "AEIOUaeiou"
    sample3 = "Python Programming"
    print(remove_vowels(sample1))
    print(remove_vowels(sample2))
    print(remove_vowels(sample3))