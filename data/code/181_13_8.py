def find_vowel_words(words):
    vowels = set("aeiouAEIOU")
    vowel_words = [word for word in words if any(char in vowels for char in word)]
    return vowel_words

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    result = find_vowel_words(sample_words)
    print(result)