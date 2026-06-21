def contains_vowel(word):
    vowels = "aeiou"
    return any(char in vowels for char in word.lower())

def extract_words_with_vowels(words_list):
    filtered_words = (word for word in words_list if contains_vowel(word))
    unique_words = {word for word in filtered_words}
    return sorted(unique_words)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "drum", "elephant", "fish"]
    result = extract_words_with_vowels(sample_list)
    print(result)