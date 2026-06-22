def count_vowels(word):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_word = "Alibaba"
    vowel_count = count_vowels(sample_word)
    print(vowel_count)