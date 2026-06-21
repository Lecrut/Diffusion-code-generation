VOWELS = "aeiouAEIOU"

def filter_vowel_words(word_list):
    return [word for word in word_list if any(char in VOWELS for char in word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(filter_vowel_words(sample_words))