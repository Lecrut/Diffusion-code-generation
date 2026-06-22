def find_first_word(words):
    return words.strip().split()[0]

if __name__ == '__main__':
    sample_words = "   hello world  "
    print(find_first_word(sample_words))