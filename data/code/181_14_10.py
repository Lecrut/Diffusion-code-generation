VOWELS = "aeiouAEIOU"

def contains_vowel(word):
    return any(char in VOWELS for char in word)

def filter_vowels(words):
    return [word for word in words if contains_vowel(word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(filter_vowels(sample_words))