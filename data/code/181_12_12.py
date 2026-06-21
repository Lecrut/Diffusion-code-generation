def contains_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return any(char in vowels for char in word.lower())

def identify_vowel_words(text):
    words = text.split()
    vowel_words = [word for word in words if contains_vowel(word)]
    return set(vowel_words)

if __name__ == '__main__':
    sample_text = "This is a test sentence with some words like apple and banana. Education is important."
    result = identify_vowel_words(sample_text)
    print(result)