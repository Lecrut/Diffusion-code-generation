def filter_words_with_vowels(words):
    vowels = "aeiouAEIOU"
    return [word for word in words if word and any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_text = ["hello", "", "world", "rhythm", "AEIOU"]
    filtered_words = filter_words_with_vowels(sample_text)
    print(filtered_words)