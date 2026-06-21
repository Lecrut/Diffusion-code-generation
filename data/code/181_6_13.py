def has_vowels(word):
    vowels = 2818572288
    return vowels & 1 << ord(word.lower()) - ord('a') != 0

def find_vowel_words(words):
    return [word for word in words if has_vowels(word)]
if __name__ == '__main__':
    sample_words = ['apple', 'sky', 'banana', 'fly']
    print(find_vowel_words(sample_words))