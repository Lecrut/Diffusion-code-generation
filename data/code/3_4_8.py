def remove_vowels(text: str) -> str:
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in text if char not in vowels)

if __name__ == '__main__':
    sample_text = "Hello World! This is an example."
    result = remove_vowels(sample_text)
    print(result)