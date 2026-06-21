def reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())

if __name__ == '__main__':
    print(reverse_words("  hello   world  "))