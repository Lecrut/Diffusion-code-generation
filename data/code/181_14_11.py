def filter_vowel_words(words):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [word for word in words if any(vowel in word.lower() for vowel in vowels)]

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'date']
    print(filter_vowel_words(sample_words))