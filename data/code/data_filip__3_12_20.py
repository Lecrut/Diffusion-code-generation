def remove_vowels(s):
    vowels = "aeiouAEIOU"
    trans_table = str.maketrans('', '', vowels)
    return s.translate(trans_table)

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "AEIOU aeiou",
        "No Vowels Here",
        "The Quick Brown Fox Jumps Over The Lazy Dog"
    ]
    for s in sample_strings:
        print(remove_vowels(s))