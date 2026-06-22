def remove_vowels(text):
    vowels = "aeiouAEIOU"
    trans_table = str.maketrans("", "", vowels)
    return text.translate(trans_table)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Python Programming"
    sample3 = "AEIOU aeiou"
    print(remove_vowels(sample1))
    print(remove_vowels(sample2))
    print(remove_vowels(sample3))