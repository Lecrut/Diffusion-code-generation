import string

def count_vowels(text):
    translation_table = str.maketrans('', '', string.ascii_lowercase[string.ascii_lowercase.index('a'):string.ascii_lowercase.index('z')+1].replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', ''))
    translation_table_upper = str.maketrans('', '', string.ascii_uppercase[string.ascii_uppercase.index('A'):string.ascii_uppercase.index('Z')+1].replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', ''))
    combined_table = translation_table
    for k, v in translation_table_upper.items():
        if k in combined_table:
            combined_table[k] = v
        else:
            combined_table[k] = v
    cleaned = text.translate(combined_table)
    vowel_table = str.maketrans('aeiouAEIOU', 'aaaaaaaaaaaa')
    return len(cleaned.translate(vowel_table))

if __name__ == '__main__':
    large_string = "Hello World! This is a test string with many vowels. Aeiou AEIOU 12345. The quick brown fox jumps over the lazy dog. Python programming is fun." * 1000
    print(count_vowels(large_string))