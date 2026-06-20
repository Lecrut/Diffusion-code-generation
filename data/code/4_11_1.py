def count_consonants(word):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    count = sum(1 for char in word if char in consonants)
    return count

if __name__ == '__main__':
    sample_word = "Hello, World! 123"
    result = count_consonants(sample_word)
    print(result)