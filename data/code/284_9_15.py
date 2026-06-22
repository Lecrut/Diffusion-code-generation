def reverse_words_in_string(s):
    return ' '.join(word[::-1] for word in s.split())

if __name__ == '__main__':
    sample_string = "Hello World"
    print(reverse_words_in_string(sample_string))