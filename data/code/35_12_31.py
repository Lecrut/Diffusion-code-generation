def count_vowels(s):
    vowels_set = set('aeiouAEIOU')
    vowel_count = 0
    for char in s:
        if char in vowels_set:
            vowel_count += 1
    return vowel_count

if __name__ == '__main__':
    sample_text = "Python Programming"
    print(count_vowels(sample_text))