def find_words_with_vowels(words):
    vowels = "aeiou"
    return sorted({word for word in words if any(char in vowels for char in word.lower())})

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date", "elderberry"]
    result = find_words_with_vowels(sample_list)
    print(result)