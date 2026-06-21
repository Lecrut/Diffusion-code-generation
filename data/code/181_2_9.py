VOWELS = set('aeiouAEIOU')

def filter_vowel_words(words):
    return [word for word in words if any(char in VOWELS for char in word)]

if __name__ == '__main__':
    test_words = ['hello', 'world', 'Python', 'programming', 'is', 'fun']
    filtered_words = filter_vowel_words(test_words)
    print(filtered_words)