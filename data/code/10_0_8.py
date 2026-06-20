def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    print(reverse_words("hello world"))
    print(reverse_words("the quick brown fox"))
    print(reverse_words("Python is great"))