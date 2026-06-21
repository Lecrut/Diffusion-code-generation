vowel_set = set("aeiouAEIOU")

def filter_vowels(words):
    return [word for word in words if any(char in vowel_set for char in word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(filter_vowels(sample_words))