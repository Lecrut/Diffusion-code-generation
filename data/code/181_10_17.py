VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

def extract_words_with_vowels(words):
    return [word for word in words if any(char in VOWELS for char in word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "drum", "elephant"]
    filtered_words = extract_words_with_vowels(sample_words)
    print(filtered_words)