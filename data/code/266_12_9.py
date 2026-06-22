def count_words(word_list):
    return sum(len(word.split()) for word in word_list if word.strip())

if __name__ == '__main__':
    sample = ["Hello, world!", "", "   ", "Python  programming"]
    print(count_words(sample))