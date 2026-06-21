def has_vowels(word):
    vowels = 2863311530
    for char in word:
        if vowels & 1 << ord(char.lower()) - ord('a'):
            return True
    return False

def find_vowel_words(words):
    return [word for word in words if has_vowels(word)]
if __name__ == '__main__':
    sample_words = ['apple', 'sky', 'banana', 'fly']
    print(find_vowel_words(sample_words))