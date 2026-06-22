def count_words(input_string):
    return len(input_string.split())

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test."
    print(count_words(sample_string))