def extract_words_with_vowels(phrases):
    vowels = "aeiouAEIOU"
    words_with_vowels = {word for phrase in phrases for word in phrase.split() if any(char in vowels for char in word)}
    return words_with_vowels

if __name__ == '__main__':
    sample_phrases = [
        "Learning Python is fun",
        "Data science and machine learning are fascinating",
        "Artificial intelligence opens up new possibilities"
    ]
    result = extract_words_with_vowels(sample_phrases)
    print(result)