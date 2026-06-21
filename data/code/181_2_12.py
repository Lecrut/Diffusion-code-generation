def contains_vowel(word):
    vowels = set('aeiouAEIOU')
    return any(char in vowels for char in word)

def filter_vowel_words(words):
    return [word for word in words if contains_vowel(word)]

if __name__ == '__main__':
    test_words = ['hello', 'world', 'Python', 'programming', 'is', 'fun']
    filtered_words = filter_vowel_words(test_words)
    print(filtered_words)