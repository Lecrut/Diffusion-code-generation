def contains_vowel(word):
    vowels = set("aeiouAEIOU")
    return any(char in vowels for char in word)

def filter_vowels(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a list of strings.")
    
    return [word for word in words if contains_vowel(word)]

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(filter_vowels(sample_words))