def count_vowels(word):
    vowels = set('aeiouAEIOU')
    vowel_count = 0
    for character in word:
        if character in vowels:
            vowel_count += 1
    return vowel_count

if __name__ == '__main__':
    sample_input = "Python Programming"
    result = count_vowels(sample_input)
    print(result)