sample_string = "  hello   world this is a test  "

def split_words(input_string):
    return input_string.split()

if __name__ == '__main__':
    words = split_words(sample_string)
    print(words)