import string

VOWEL_TABLE = bytearray.maketrans(b'', b'', b'aeiouAEIOU')

def count_vowels(s):
    return len(s) - len(s.translate(VOWEL_TABLE))

if __name__ == '__main__':
    large_string = "Hello World! This is a test string with vowels and consonants. " * 10000
    result = count_vowels(large_string)
    print(result)