def reverse_word_order(text):
    return ' '.join(text.split()[::-1])

if __name__ == '__main__':
    print(reverse_word_order('Hello World from Python'))