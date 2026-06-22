def count_consonants(word: str) -> int:
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    return sum(1 for char in word if char in consonants)

if __name__ == '__main__':
    sample_word = "Hello, World!"
    result = count_consonants(sample_word)
    print(result)