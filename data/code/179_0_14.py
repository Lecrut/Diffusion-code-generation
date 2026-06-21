def reverse_words(s):
    return ' '.join(s.split()[::-1])
if __name__ == '__main__':
    print(reverse_words('hello world'))
    print(reverse_words('the quick brown fox jumps over the lazy dog'))