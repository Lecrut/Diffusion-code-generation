def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    translation_table = str.maketrans({v: None for v in vowels})
    return s.translate(translation_table)

if __name__ == '__main__':
    sample_input = "Hello World"
    result = remove_vowels(sample_input)
    print(result)