def reverse_word_order(s):
    words = s.split()
    return ' '.join(reversed(words))

if __name__ == '__main__':
    print(reverse_word_order("Hello World"))
    print(reverse_word_order("Python is great"))
    print(reverse_word_order("one"))