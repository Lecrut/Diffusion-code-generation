def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    result = []
    for char in text:
        if char not in vowels:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "Hello World"
    output = remove_vowels(sample_input)
    print(output)