import string

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    trans_table = str.maketrans('', '', vowels)
    return s.translate(trans_table)

if __name__ == '__main__':
    sample = "Hello World"
    print(remove_vowels(sample))