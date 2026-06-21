def reverse_words(s):
    return ' '.join(word for word in s.split()[::-1])

if __name__ == '__main__':
    sample_input = "  hello   world! this is a test.  "
    print(reverse_words(sample_input))