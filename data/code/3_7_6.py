def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    return ''.join([char for char in text if char not in vowels])

if __name__ == '__main__':
    sample_text = "Hello, World! This is a sample string with vowels."
    result = remove_vowels(sample_text)
    print(result)