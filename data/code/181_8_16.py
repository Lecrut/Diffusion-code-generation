VOWELS = "aeiouAEIOU"

def filter_words_with_vowels(words):
    return [word for word in words if any(char in VOWELS for char in word) and len(word.strip()) > 0]

if __name__ == '__main__':
    sample_text = ["apple", "", "banana", " ", "cherry"]
    filtered_words = filter_words_with_vowels(sample_text)
    print(filtered_words)