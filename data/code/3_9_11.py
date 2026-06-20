import string

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    trans_table = str.maketrans('', '', vowels)
    return s.translate(trans_table)

if __name__ == '__main__':
    print(remove_vowels("Hello World"))
    print(remove_vowels("Python Programming"))
    print(remove_vowels("AEIOU aeiou"))