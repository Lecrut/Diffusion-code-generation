def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    trans_table = str.maketrans('', '', vowels)
    return s.translate(trans_table)

if __name__ == '__main__':
    sample = "Hello World!"
    print(remove_vowels(sample))
    sample2 = "Python Programming"
    print(remove_vowels(sample2))
    sample3 = "AEIOUaeiou"
    print(remove_vowels(sample3))
    sample4 = "No vowels here"
    print(remove_vowels(sample4))