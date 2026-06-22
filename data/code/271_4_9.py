def word_with_most_vowels(words):
    vowels = 'aeiou'
    max_vowel_count = 0
    word_with_max_vowels = ''
    
    for word in words:
        vowel_count = sum(1 for char in word.lower() if char in vowels)
        if vowel_count > max_vowel_count:
            max_vowel_count = vowel_count
            word_with_max_vowels = word
    
    return word_with_max_vowels

if __name__ == '__main__':
    sample_words = ['hello', 'world', 'algorithm', 'data']
    print(word_with_most_vowels(sample_words))