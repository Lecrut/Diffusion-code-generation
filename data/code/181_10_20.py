def contains_vowel(word):
    vowels = "aeiouAEIOU"
    return any(vowel in word for vowel in vowels)

def extract_words_with_vowels(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a list of strings")
    
    return [word for word in words if contains_vowel(word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "grape", "kiwi"]
    print(extract_words_with_vowels(sample_words))