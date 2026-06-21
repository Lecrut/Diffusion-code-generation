def filter_vowel_words(words: list[str]) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [word for word in words if any(vowel in word for vowel in vowels)]

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'drum', 'elephant']
    print(filter_vowel_words(sample_words))