def reverse_word_order(text):
    return ' '.join(reversed(text.split()))

if __name__ == '__main__':
    print(reverse_word_order('Hello World from Python'))