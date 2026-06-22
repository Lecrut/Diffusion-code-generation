def first_word(words):
    return words.split()[0]

if __name__ == '__main__':
    sample = "  hello   world "
    print(first_word(sample))