def reverse_word_order(s):
    return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    print(reverse_word_order('Python is awesome'))