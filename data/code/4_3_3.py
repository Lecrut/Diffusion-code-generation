def count_consonants(text):
    vowels = set('aeiouAEIOU')
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    return consonant_count

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = count_consonants(sample_text)
    print(result)