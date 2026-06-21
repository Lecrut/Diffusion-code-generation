def filter_vowel_words(words):
    vowels = set('aeiouAEIOU')
    return [word for word in words if any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'drum', 'elephant']
    filtered_words = filter_vowel_words(sample_words)
    print(filtered_words)