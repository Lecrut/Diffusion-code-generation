def count_consonants(word):
    CONSONANTS = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    return sum(1 for char in word if char in CONSONANTS)

if __name__ == '__main__':
    sample_word = "Hello World"
    result = count_consonants(sample_word)
    print(result)