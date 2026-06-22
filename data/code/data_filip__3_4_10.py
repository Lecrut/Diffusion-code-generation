def remove_vowels(text):
    return ''.join(char for char in text if char.lower() not in 'aeiou')

if __name__ == '__main__':
    sample = "Hello World"
    print(remove_vowels(sample))