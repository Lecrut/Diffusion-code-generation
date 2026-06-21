def reverse_words(sentence):
    return ' '.join(reversed(sentence.split()))

if __name__ == '__main__':
    print(reverse_words('AI helps coding'))