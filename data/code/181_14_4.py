def filter_vowels(words):
    vowels = set("aeiouAEIOU")
    return [word for word in words if any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(filter_vowels(sample_words))