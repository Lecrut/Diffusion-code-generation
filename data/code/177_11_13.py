sample_string = "   This is a    sample string with  multiple spaces.   "

def separate_words(input_string):
    return input_string.split()

if __name__ == '__main__':
    words = separate_words(sample_string)
    print(words)