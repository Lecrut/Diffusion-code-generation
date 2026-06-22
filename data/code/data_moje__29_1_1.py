VOWEL_SET = {'a', 'e', 'i', 'o', 'u'}
count_vowels = lambda text: len([ch for ch in text.lower() if ch in VOWEL_SET])
if __name__ == '__main__':
    test_string = "Programming is fascinating"
    print(count_vowels(test_string))