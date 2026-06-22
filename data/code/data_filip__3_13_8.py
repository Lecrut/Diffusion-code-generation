def remove_vowels(text):
    return ''.join(c for c in text if c.lower() not in 'aeiou')

if __name__ == '__main__':
    sample = "Hello World"
    print(remove_vowels(sample))