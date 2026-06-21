def has_vowels(word):
    vowels = 2863311530
    return any((vowels & 1 << ord(c) - ord('a') for c in word.lower()))

def find_vowel_words(words):
    return [word for word in words if has_vowels(word)]
if __name__ == '__main__':
    sample_words = ['apple', 'sky', 'umbrella', 'fly']
    print(find_vowel_words(sample_words))