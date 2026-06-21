vowels = set("aeiouAEIOU")

def filter_vowel_words(words):
    return [word for word in words if any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(filter_vowel_words(sample_words))