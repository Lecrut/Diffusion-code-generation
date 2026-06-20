def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    return ''.join([char for char in text if char not in vowels])

if __name__ == '__main__':
    sample_string = "Hello World! This is a test string."
    result = remove_vowels(sample_string)
    print(result)