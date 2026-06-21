import string

def count_vowels(text):
    if not text:
        return 0
    
    vowels = 'aeiouAEIOU'
    trans_table = str.maketrans(vowels, '1' * 10 + '1' * 10)
    translated = text.translate(trans_table)
    
    return translated.count('1')

if __name__ == '__main__':
    sample_string = "The quick brown fox jumps over the lazy dog and flies home."
    result = count_vowels(sample_string)
    print(result)