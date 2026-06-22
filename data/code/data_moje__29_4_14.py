def count_vowels(text):
    vowels = set('aeiouAEIOU')
    unique_chars = set(text)
    return len(unique_chars.intersection(vowels))

if __name__ == '__main__':
    sample = "Hello World"
    print(count_vowels(sample))
    sample2 = "xyz"
    print(count_vowels(sample2))
    sample3 = "A E I O U"
    print(count_vowels(sample3))