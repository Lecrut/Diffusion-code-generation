def word_with_most_vowels(words):
    vowels = 'aeiou'
    max_vowel_count = 0
    result_word = ''
    
    for word in words:
        vowel_count = sum(1 for char in word.lower() if char in vowels)
        if vowel_count > max_vowel_count:
            max_vowel_count = vowel_count
            result_word = word
    
    return result_word

if __name__ == '__main__':
    sample_words = ['hello', 'world', 'example', 'test']
    print(word_with_most_vowels(sample_words))