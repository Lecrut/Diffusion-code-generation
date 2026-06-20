def count_consonants(word: str) -> int:
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in word:
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_word = "Programming"
    result = count_consonants(sample_word)
    print(result)