def count_consonants(word):
    return len(list(filter(lambda c: c.lower() in 'bcdfghjklmnpqrstvwxyz', word)))

if __name__ == '__main__':
    sample_word = "hello"
    print(count_consonants(sample_word))