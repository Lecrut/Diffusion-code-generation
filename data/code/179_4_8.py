def reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())

if __name__ == '__main__':
    sample_string = "  Hello   world! "
    print(reverse_words(sample_string))