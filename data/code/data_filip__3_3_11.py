def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    return ''.join(char for char in text if char not in vowels)

if __name__ == '__main__':
    sample_input = "Hello World"
    result = remove_vowels(sample_input)
    print(result)