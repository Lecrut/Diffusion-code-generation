def extract_words_with_vowels(words):
    vowels = set('aeiouAEIOU')
    return [word for word in words if any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'drum', 'elephant']
    filtered_words = extract_words_with_vowels(sample_words)
    print(filtered_words)