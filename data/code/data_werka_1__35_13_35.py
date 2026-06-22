def count_vowels(word):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in word if char in vowels)

if __name__ == '__main__':
    sample_word = "AlibabaCloud"
    vowel_count = count_vowels(sample_word)
    print(vowel_count)