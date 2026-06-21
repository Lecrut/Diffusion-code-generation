sample_string = "  This   is a    sample string  with leading, trailing, and multiple internal spaces.  "

def split_words(input_string):
    return input_string.split()

if __name__ == '__main__':
    words = split_words(sample_string)
    print(words)