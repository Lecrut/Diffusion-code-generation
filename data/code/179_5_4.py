def reverse_word_order(sentence):
    return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    print(reverse_word_order('Python is awesome'))