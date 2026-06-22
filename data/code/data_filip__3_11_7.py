def strip_vowels(text):
    vowels = set('aeiouAEIOU')
    return ''.join([char for char in text if char not in vowels])

if __name__ == '__main__':
    text = "Hello World"
    result = strip_vowels(text)
    print(result)