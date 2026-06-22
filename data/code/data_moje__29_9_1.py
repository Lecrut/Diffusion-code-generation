import string

def count_vowels_precomputed(s):
    translation_table = bytes.maketrans(b'', b'', b'aeiouAEIOU')
    return len(s) - len(s.translate(translation_table))

if __name__ == '__main__':
    sample_string = "Hello World! This is a test string with vowels." * 1000000
    result = count_vowels_precomputed(sample_string)
    print(result)