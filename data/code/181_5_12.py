def extract_words_with_vowels(phrases):
    vowels = "aeiouAEIOU"
    words_with_vowels = set(word for phrase in phrases for word in phrase.split() if any(char in vowels for char in word.strip(".,!?")))
    return words_with_vowels

if __name__ == '__main__':
    sample_phrases = [
        "Programming is awesome",
        "Python is fun and powerful",
        "Data science is exciting"
    ]
    result = extract_words_with_vowels(sample_phrases)
    print(result)