def count_consonants(word):
    consonants = set('bcdfghjklmnpqrstvwxyz')
    count = 0
    for char in word.lower():
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_word = "HelloWorld"
    result = count_consonants(sample_word)
    print(result)