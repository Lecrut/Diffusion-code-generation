def count_consonants(text: str) -> int:
    vowels = set('aeiouAEIOU')
    return len([char for char in text if char.isalpha() and char not in vowels])

if __name__ == '__main__':
    sample_text = "Hello, World! This is a sample text."
    result = count_consonants(sample_text)
    print(result)