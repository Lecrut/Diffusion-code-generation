def remove_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = []
    for char in text:
        if char not in vowels:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "Hello World"
    print(remove_vowels(sample_text))