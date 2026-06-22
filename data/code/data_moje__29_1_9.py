lambda text: sum(1 for char in text.lower() if char in 'aeiou')

if __name__ == '__main__':
    count_vowels = lambda text: sum(1 for char in text.lower() if char in 'aeiou')
    sample_text = "Hello World"
    print(count_vowels(sample_text))