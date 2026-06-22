def count_consonants(text):
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    return sum(1 for char in text if char in consonants)

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    print(count_consonants(sample_text))