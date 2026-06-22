def count_consonants(word):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in word:
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_words = ["Hello", "World", "Python", "AEIOU", "Code"]
    for word in sample_words:
        result = count_consonants(word)
        print(f"{word}: {result}")