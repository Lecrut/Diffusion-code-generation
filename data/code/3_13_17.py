def remove_vowels(text):
    return ''.join(char for char in text if char.lower() not in 'aeiou')

if __name__ == '__main__':
    sample_text = "Hello World! How are you today?"
    result = remove_vowels(sample_text)
    print(result)