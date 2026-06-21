def filter_words_with_vowels(words):
    vowels = set('aeiouAEIOU')
    return [word for word in words if word.strip() and any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_text = ["hello", "", "world", " ", "python", "is", "awesome"]
    filtered_words = filter_words_with_vowels(sample_text)
    print(filtered_words)