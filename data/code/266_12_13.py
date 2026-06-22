def count_words(words):
    return sum(len(word.split()) for word in words if word.strip())

if __name__ == '__main__':
    sample = ["Hello, world!", "", "   ", "Python  programming"]
    print(count_words(sample))