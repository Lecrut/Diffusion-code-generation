def count_vowels(s):
    translation_table = str.maketrans('aeiouAEIOU', '1111111111')
    return s.translate(translation_table).count('1')

if __name__ == '__main__':
    sample_string = "The Quick Brown Fox Jumps Over The Lazy Dog. Aeiou Aeiou"
    result = count_vowels(sample_string)
    print(result)