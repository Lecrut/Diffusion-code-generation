def word_generator(text):
    import re
    words = re.findall(r'\w+', text)
    for word in words:
        yield word
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with some special characters 123."
    generator = word_generator(sample_string)
    result_list = list(generator)
    print(result_list)