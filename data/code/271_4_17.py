def count_vowels(word):
    vowels = 'aeiou'
    return sum(1 for char in word if char.lower() in vowels)

def word_with_most_vowels(words):
    max_vowel_count = 0
    word_with_max_vowels = ''
    for word in words:
        vowel_count = count_vowels(word)
        if vowel_count > max_vowel_count:
            max_vowel_count = vowel_count
            word_with_max_vowels = word
    return word_with_max_vowels

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'date']
    print(word_with_most_vowels(sample_words))