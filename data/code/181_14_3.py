def filter_vowel_words(word_list):
    vowels = "aeiouAEIOU"
    return [word for word in word_list if any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    result = filter_vowel_words(sample_words)
    print(result)