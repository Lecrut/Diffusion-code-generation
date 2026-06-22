def remove_vowels(s):
    vowel_map = str.maketrans('', '', 'aeiouAEIOU')
    return s.translate(vowel_map)

if __name__ == '__main__':
    sample = "Hello World"
    result = remove_vowels(sample)
    print(result)