def filter_vowel_words(words):
    vowels = set('aeiouAEIOU')
    return [word for word in words if any(char in vowels for char in word)]

if __name__ == '__main__':
    test_input = ['hello', 'world', 'Python', 'programming', 'is', 'fun']
    expected_output = ['hello', 'world', 'Python', 'programming', 'is']
    assert filter_vowel_words(test_input) == expected_output
    print(filter_vowel_words(test_input))