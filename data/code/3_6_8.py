def eliminate_vowels(text):
    vowels = 'aeiouAEIOU'
    filtered_chars = filter(lambda char: char not in vowels, text)
    return ''.join(filtered_chars)

if __name__ == '__main__':
    result = eliminate_vowels("Hello World")
    print(result)