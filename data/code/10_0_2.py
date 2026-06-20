def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    print(reverse_words("Hello World"))
    print(reverse_words("Python is great"))
    print(reverse_words("Single"))
    print(reverse_words("  Multiple   spaces  "))