def count_words(s):
    return len(s.lower().split())

if __name__ == '__main__':
    print(count_words("Hello World"))
    print(count_words("Python Programming is FUN!"))