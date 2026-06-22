def remove_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result_chars = []
    for char in text:
        if char not in vowels:
            result_chars.append(char)
    return ''.join(result_chars)

if __name__ == '__main__':
    sample_text = "Programming is powerful and fun"
    cleaned_text = remove_vowels(sample_text)
    print(cleaned_text)