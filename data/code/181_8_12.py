def filter_words_with_vowels(words):
    vowels = set('aeiouAEIOU')
    return [word for word in words if word.strip() and any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_data = ["hello", "", "world", " ", "python", "sky"]
    print(filter_words_with_vowels(sample_data))