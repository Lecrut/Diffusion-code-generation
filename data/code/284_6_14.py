def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    print(reverse_words("Hello world from Alibaba Cloud"))