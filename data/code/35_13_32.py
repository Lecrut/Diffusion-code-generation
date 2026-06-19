def count_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel_count = 0
    for char in word:
        if char in vowels:
            vowel_count += 1
    return vowel_count

if __name__ == '__main__':
    sample_word = "Alibaba Cloud"
    print(count_vowels(sample_word))