VOWELS = set('aeiouAEIOU')

def contains_vowel(word):
    return any(char in VOWELS for char in word)

def extract_words_with_vowels(words):
    return [word for word in words if contains_vowel(word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "drum", "echo"]
    filtered_words = extract_words_with_vowels(sample_words)
    print(filtered_words)