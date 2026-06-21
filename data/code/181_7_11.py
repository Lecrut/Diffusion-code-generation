def find_words_with_vowels(words):
    vowels = set('aeiouAEIOU')
    return sorted({word for word in words if any(char in vowels for char in word)})

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    print(find_words_with_vowels(sample_words))