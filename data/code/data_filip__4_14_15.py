def count_consonants(word):
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    count = 0
    for char in word.lower():
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_word = "Python"
    result = count_consonants(sample_word)
    print(result)