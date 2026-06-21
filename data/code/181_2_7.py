def contains_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return any(char in vowels for char in word)

def filter_vowel_words(words):
    return [word for word in words if contains_vowel(word)]

if __name__ == '__main__':
    sample_words = ['hello', 'world', 'Python', 'programming', 'is', 'fun']
    filtered_words = filter_vowel_words(sample_words)
    print(filtered_words)