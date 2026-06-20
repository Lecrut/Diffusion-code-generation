import string

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    trans_table = str.maketrans('', '', vowels)
    return text.translate(trans_table)

if __name__ == '__main__':
    sample = "Hello World!"
    print(remove_vowels(sample))
    sample2 = "Python is AWESOME"
    print(remove_vowels(sample2))
    sample3 = "No vowels here if we remove them all!"
    print(remove_vowels(sample3))