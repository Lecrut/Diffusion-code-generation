def count_words(s):
    return len(s.split())

if __name__ == '__main__':
    sample_string = "Hello World! This is a test."
    print(count_words(sample_string.lower()))