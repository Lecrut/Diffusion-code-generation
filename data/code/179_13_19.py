def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    test_string = "hello world this is a test"
    result = reverse_words(test_string)
    print(result)