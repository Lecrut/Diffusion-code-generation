def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    return ''.join(char for char in text if char not in vowels)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)