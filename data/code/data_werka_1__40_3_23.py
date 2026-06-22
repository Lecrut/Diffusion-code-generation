def first_letters(s):
    return ' '.join(word[0] for word in s.split())

if __name__ == '__main__':
    print(first_letters("The quick brown fox jumps over the lazy dog"))