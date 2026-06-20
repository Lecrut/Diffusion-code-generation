def count_consonants(text):
    vowels = "aeiouAEIOU"
    return len([char for char in text if char.isalpha() and char not in vowels])

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = count_consonants(sample_text)
    print(result)