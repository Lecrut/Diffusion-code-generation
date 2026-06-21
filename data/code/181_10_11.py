def contains_vowel(word):
    vowels = set('aeiouAEIOU')
    return any(char in vowels for char in word)

def extract_words_with_vowels(words):
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements in the input list must be strings.")
    
    return [word for word in words if contains_vowel(word)]

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'drum', 'elephant']
    print(extract_words_with_vowels(sample_words))