def count_consonants(word):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    count = 0
    for char in word:
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_word = "Hello World"
    result = count_consonants(sample_word)
    print(result)