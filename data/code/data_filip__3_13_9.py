def remove_vowels(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    vowels = set('aeiouAEIOU')
    return ''.join(char for char in text if char not in vowels)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)