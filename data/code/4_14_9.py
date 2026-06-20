def count_consonants(word):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    return sum(1 for char in word if char in consonants)

if __name__ == '__main__':
    word = "Python"
    result = count_consonants(word)
    print(result)