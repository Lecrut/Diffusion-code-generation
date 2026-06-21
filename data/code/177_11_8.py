sample_string = "  This   is a    sample string  "

def split_words(input_string):
    return input_string.split()

if __name__ == '__main__':
    result = split_words(sample_string)
    print(result)