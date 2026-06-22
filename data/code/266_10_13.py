def count_words(input_string):
    return len(input_string.split())

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string."
    print(count_words(sample_string))