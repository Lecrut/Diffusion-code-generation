if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with various spaces and punctuation."
    words = [word for word in sample_string.split() if word]
    print(words)