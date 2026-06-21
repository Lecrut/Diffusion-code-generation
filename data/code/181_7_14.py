def contains_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return any(char in vowels for char in word.lower())

def filter_words_with_vowels(words):
    return (word for word in words if contains_vowel(word))

def unique_sorted_words(words):
    return sorted(set(words))

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date", "fig", "grape"]
    filtered_words = filter_words_with_vowels(sample_list)
    unique_sorted_words = unique_sorted_words(filtered_words)
    print(unique_sorted_words)