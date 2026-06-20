def count_consonants(word):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    return len([1 for char in word if char in consonants])

if __name__ == '__main__':
    result = count_consonants("Hello World!")
    print(result)