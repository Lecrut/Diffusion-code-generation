def reverse_words(s):
    return ' '.join(reversed(s.split()))

if __name__ == '__main__':
    print(reverse_words("Hello World"))