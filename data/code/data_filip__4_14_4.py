def count_consonants(word):
    consonants = set('bcdfghjklmnpqrstvwxyz')
    return sum(1 for char in word.lower() if char in consonants)

if __name__ == '__main__':
    sample_word = "HelloWorld"
    print(count_consonants(sample_word))