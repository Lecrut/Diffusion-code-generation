def any_word_longer_than_six(s):
    return any(len(word) > 6 for word in s.split())

if __name__ == '__main__':
    print(any_word_longer_than_six("hello world"))
    print(any_word_longer_than_six("Python programming is fun"))