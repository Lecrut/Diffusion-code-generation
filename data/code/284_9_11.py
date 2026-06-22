def reverse_words_in_string(s):
    return ' '.join(word[::-1] for word in s.split())

if __name__ == '__main__':
    sample = "Hello world from Python"
    print(reverse_words_in_string(sample))