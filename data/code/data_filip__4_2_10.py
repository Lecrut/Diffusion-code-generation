def count_consonants():
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    text = 'The quick brown fox jumps over the lazy dog'
    return sum(1 for char in text if char in consonants)

if __name__ == '__main__':
    print(count_consonants())