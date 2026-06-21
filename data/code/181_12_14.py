def identify_vowel_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.lower().split()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_words = {word for word in words if any(char in vowels for char in word)}
    return vowel_words

if __name__ == '__main__':
    sample_text = "This is a test sentence with many words including apple and banana."
    result = identify_vowel_words(sample_text)
    print(result)