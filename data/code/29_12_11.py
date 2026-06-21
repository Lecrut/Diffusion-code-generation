def count_vowels(text):
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    sample_text = "Hello World, this is a sample string with vowels."
    print(count_vowels(sample_text))