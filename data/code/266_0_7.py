def count_words(input_string):
    words = input_string.split()
    return len(words)

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test."
    print(count_words(sample_string))