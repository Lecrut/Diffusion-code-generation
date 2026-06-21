def reverse_word_order(s):
    return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    sample = 'Python is awesome'
    print(reverse_word_order(sample))