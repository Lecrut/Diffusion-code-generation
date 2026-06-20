def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in text if char not in vowels)

if __name__ == '__main__':
    sample_text = "Hello World, this is a test."
    result = remove_vowels(sample_text)
    print(result)