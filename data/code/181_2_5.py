def filter_vowel_words(words):
    vowels = set('aeiouAEIOU')
    return [word for word in words if any(vow in word for vow in vowels)]

if __name__ == '__main__':
    test_words = ['hello', 'world', 'Python', 'is', 'awesome']
    print(filter_vowel_words(test_words))