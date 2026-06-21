sample_string = "  This   is  a    sample   string  "

def separate_words(input_string):
    return input_string.split()

if __name__ == '__main__':
    result = separate_words(sample_string)
    print(result)