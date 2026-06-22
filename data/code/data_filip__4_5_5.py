def count_consonants(word):
    return len(list(filter(lambda c: c.lower() not in 'aeiou' and c.isalpha(), word)))

if __name__ == '__main__':
    word = "Python"
    print(count_consonants(word))