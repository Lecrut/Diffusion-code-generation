def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    return ''.join(char for char in text if char not in vowels)

if __name__ == '__main__':
    sample_text = "Hello World! This is a robust Python function for large-scale text processing."
    result = remove_vowels(sample_text)
    print(result)