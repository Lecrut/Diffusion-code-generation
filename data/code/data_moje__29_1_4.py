count_vowels = lambda text: sum(1 for char in text.lower() if char in 'aeiou')
if __name__ == '__main__':
    sample_text = "Hello World, this is a test."
    print(count_vowels(sample_text))