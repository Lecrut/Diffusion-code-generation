def count_consonants(text):
    vowels = set('aeiouAEIOU')
    consonants = set(
        c for c in text
        if c.isalpha() and c not in vowels
    )
    return sum(1 for c in text if c in consonants)

if __name__ == '__main__':
    sample = "Hello World! 你好世界 café naïve"
    print(count_consonants(sample))