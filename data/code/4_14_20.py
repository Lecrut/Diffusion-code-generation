def count_consonants(word):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    return sum(1 for char in word if char in consonants)

if __name__ == '__main__':
    result = count_consonants("Python")
    print(result)