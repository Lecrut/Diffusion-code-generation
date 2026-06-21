def reverse_words(s):
    return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    sample = "Hello world from Python"
    print(reverse_words(sample))