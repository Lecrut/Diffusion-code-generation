def count_consonants(word):
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    count = 0
    for char in word:
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_words = ["hello", "python", "rhythm", "aeiou", "sk8"]
    for word in sample_words:
        result = count_consonants(word)
        print(result)