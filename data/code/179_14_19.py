def reverse_words(s):
    return ' '.join(word for word in s.split()[::-1])

if __name__ == '__main__':
    print(reverse_words("  Hello   world!  "))