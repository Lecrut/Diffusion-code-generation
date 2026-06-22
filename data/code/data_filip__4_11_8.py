def count_consonants(word):
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    return len([c for c in word.lower() if c in consonants])

if __name__ == '__main__':
    result = count_consonants("Hello World")
    print(result)