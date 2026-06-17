def punctuation_generator(text):
    for char in text:
        if char in '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~':
            yield char
if __name__ == '__main__':
    large_string = "This is a test string with many punctuation marks! ... and more symbols like ?, ., and :"
    punctuation_stream = punctuation_generator(large_string)
    result_list = list(punctuation_stream)
    print(result_list)