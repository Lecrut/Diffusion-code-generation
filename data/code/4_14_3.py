def count_consonants(word: str) -> int:
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for char in word.lower():
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_word = "Python"
    result = count_consonants(sample_word)
    print(result)